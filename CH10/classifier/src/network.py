import numpy as np

class Network:

    def __init__(self, params):
        self.params = params
        self.input_size = params.Shapes.image_size**2
        self.hidden_size = params.Network.hidden_size
        self.output_size = len(params.Shapes.category_list)
        self.l2_lambda = params.Network.l2_lambda
        self.weight_mean = 0
        self.weight_stdev = 0.0001

        self.h_bias = None
        self.h_x = None
        self.o_bias = None
        self.o_h = None

        self.train_cost = None
        self.train_accuracy = None
        self.train_confusion_matrix = None

        self.test_cost = None
        self.test_accuracy = None
        self.test_confusion_matrix = None

        self.epoch = None  # Initialize epoch counter

        self.init_network()

    def init_network(self):
        # Xavier initialization for hidden weights
        limit_h_x = np.sqrt(6 / (self.input_size + self.hidden_size))
        self.h_x = np.random.uniform(-limit_h_x, limit_h_x, (self.hidden_size, self.input_size))
        self.h_bias = np.full(self.hidden_size, 0.01)  # Set bias to a small value

        # Xavier initialization for output weights
        limit_o_h = np.sqrt(6 / (self.hidden_size + self.output_size))
        self.o_h = np.random.uniform(-limit_o_h, limit_o_h, (self.output_size, self.hidden_size))
        self.o_bias = np.full(self.output_size, 0.01)  # Set bias to a small value

        self.epoch = 0

    def forward(self, x):
        if x.ndim == 1:
            # Single input vector
            zh = np.dot(self.h_x, x) + self.h_bias
            h = np.tanh(zh)
            zo = np.dot(self.o_h, h) + self.o_bias
        elif x.ndim == 2:
            # Batch of input vectors
            zh = np.dot(x, self.h_x.T) + self.h_bias  # Transpose h_x for batch processing
            h = np.tanh(zh)
            zo = np.dot(h, self.o_h.T) + self.o_bias  # Transpose o_h for batch processing
        else:
            raise ValueError(f"Unsupported input shape: {x.shape}")

        # Softmax normalization for output layer
        exp_zo = np.exp(zo - np.max(zo, axis=-1, keepdims=True))  # Stability fix
        o = exp_zo / exp_zo.sum(axis=-1, keepdims=True)

        return h, o

    def calc_cost(self, y, o):
        # Cross-entropy loss with L2 regularization
        epsilon = 1e-12
        o = np.clip(o, epsilon, 1. - epsilon)
        base_cost = -np.sum(y * np.log(o)) / y.shape[0]

        # Add L2 regularization penalty
        l2_penalty = (self.l2_lambda / 2) * (np.sum(np.square(self.h_x)) + np.sum(np.square(self.o_h)))
        return base_cost + l2_penalty

    def backpropagation(self, x, o, h, y, learning_rate):
        # Multiclass cross-entropy gradient for output layer
        o_delta = o - y  # Gradient for cross-entropy with softmax

        # Calculate hidden layer gradients
        h_cost = np.dot(o_delta, self.o_h)
        h_delta = h_cost * (1 - h ** 2)

        # Update weights and biases with L2 regularization
        self.o_bias -= learning_rate * o_delta
        self.o_h -= learning_rate * (np.outer(o_delta, h) + self.l2_lambda * self.o_h)

        self.h_bias -= learning_rate * h_delta
        self.h_x -= learning_rate * (np.outer(h_delta, x) + self.l2_lambda * self.h_x)

    def train(self, training_set, learning_rate, batch_size=32, test_set=None):
        num_samples = len(training_set.x_list)
        num_batches = num_samples // batch_size

        for batch_idx in range(num_batches):
            batch_x = training_set.x_list[batch_idx * batch_size:(batch_idx + 1) * batch_size]
            batch_y = training_set.y_list[batch_idx * batch_size:(batch_idx + 1) * batch_size]

            # Accumulate gradients and apply updates for each mini-batch
            for x, y in zip(batch_x, batch_y):
                x = training_set.add_noise(x)  # Apply noise if needed
                h, o = self.forward(x)
                self.backpropagation(x, o, h, y, learning_rate)
        self.epoch += 1
        # Regularly output progress
        if self.epoch % self.params.Network.output_freq == 0:
            self.evaluate(training_set, test_set)

    def evaluate(self, training_set, test_set):
        self.train_cost, self.train_accuracy, self.train_confusion_matrix = self.test(training_set)
        if test_set:
            self.test_cost, self.test_accuracy, self.test_confusion_matrix = self.test(test_set)
        print(
            f"Epoch {self.epoch}\tCost (Train/Test): {self.train_cost:.3f}/{'N/A' if self.test_cost is None else self.test_cost:.3f}\t"
            f"Accuracy (Train/Test): {self.train_accuracy:.3f}/{'N/A' if self.test_accuracy is None else self.test_accuracy:.3f}"
        )

    def test(self, dataset):
        confusion_matrix = np.zeros([dataset.num_categories, dataset.num_categories])
        cost_array = np.zeros([dataset.num_categories])
        n_array = np.zeros([dataset.num_categories])
        num_items = len(dataset.x_list)
        cost_sum = 0
        for i in range(num_items):
            h, o = self.forward(dataset.x_list[i])
            cost = self.calc_cost(dataset.y_list[i], o)
            cost_sum += cost
            correct_index = np.argmax(dataset.y_list[i])
            guess_index = np.argmax(o)
            cost_array[correct_index] += cost
            confusion_matrix[guess_index, correct_index] += 1
            n_array[correct_index] += 1

        prop_correct =  np.trace(confusion_matrix)/confusion_matrix.sum()
        mean_cost = cost_sum / num_items

        return mean_cost, prop_correct, confusion_matrix
