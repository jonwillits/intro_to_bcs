import numpy as np

class NeuralNetwork:

    def __init__(self):
        pass

    def get_loss(self, y_predict, yi):
        # Compute binary cross-entropy cost
        # epsilon = 1e-8  # To avoid log(0)
        # y_predict_clipped = np.clip(y_predict, epsilon, 1 - epsilon)  # Ensure y_predict is within (0,1)
        # y_cost = -(yi * np.log(y_predict_clipped) + (1 - yi) * np.log(1 - y_predict_clipped))
        y_cost = 0
        # Compute the error (target - prediction)
        error = yi - y_predict
        return y_cost, error

class Layer:

    def __init__(self, input_size, output_size, layer_name):
        self.input_size = input_size
        self.output_size = output_size
        self.name = layer_name
        self.bias = None
        self.weights = None

        self.init_weights()

    def init_weights(self):
        self.bias = np.random.normal(0, 0.5, [1, self.output_size])
        self.weights = np.random.normal(0, 0.5, [self.output_size, self.input_size])

    def forward(self, x):
        z = np.dot(x, self.weights.transpose()) + self.bias
        y = 1 / (1 + np.exp(-z))
        return z, y


class BetterNetwork(NeuralNetwork):

    def __init__(self, params, training_set):
        super().__init__()
        self.params = params
        self.training_set = training_set
        self.layer_list = None

        self.init_network()

    def init_network(self):
        self.layer_list = []
        input_size = self.training_set.shape[0]
        if self.params.hidden_size_list is not None:
            for i, hidden_size in enumerate(self.params.hidden_size_list):
                layer_name = f"h{i + 1}"
                self.layer_list.append(Layer(input_size, hidden_size, layer_name))
                input_size = hidden_size
        self.layer_list.append(Layer(input_size, self.training_set.shape[1], "Output"))

    def train(self, training_set, test_set):
        for epoch in range(self.params.num_epochs):
            cost_sum = 0
            x_size = training_set.shape[0]

            for i in range(x_size):
                xi = training_set.x[i]
                yi = training_set.y[i]

                # Forward pass
                z_list, y_predict_list = self.forward(xi)
                y_predict = y_predict_list[-1]

                # Compute loss
                y_cost, error = self.get_loss(y_predict, yi)
                cost_sum += np.mean(y_cost)

                # Get Gradients and Backpropagate
                self.backpropagate(y_predict_list, z_list, error)

                # Update Weights for all layers
                self.update(xi, self.params.learning_rate)

            if epoch % self.params.eval_freq == 0:
                mean_cost = cost_sum / x_size
                training_accuracy = self.evaluate(training_set)
                test_accuracy = self.evaluate(test_set)
                print(f"{epoch}\t{mean_cost:0.3f}\t{training_accuracy:0.3f}\t{test_accuracy:0.3f}")

    def forward(self, x):
        z_list, y_predict_list = [], []
        for layer in self.layer_list:
            z, x = layer.forward(x)
            z_list.append(z)
            y_predict_list.append(x)
        return z_list, y_predict_list

    def backpropagate(self, y_predict_list, z_list, error):
        # Backpropagate error starting from the last layer (output)
        delta = error  # Error at the output layer
        for i in reversed(range(len(self.layer_list))):
            layer = self.layer_list[i]
            y_predict = y_predict_list[i]

            # Compute gradient (Sigmoid prime)
            sigmoid_prime = y_predict * (1 - y_predict)
            y_delta = delta * sigmoid_prime  # Use delta for gradient

            # Store the gradients in the layer for updating later
            layer.y_delta = y_delta

            if i > 0:
                # Compute the error for the previous layer using the weights of the current layer
                delta = np.dot(y_delta, layer.weights)

    def update(self, xi, learning_rate):
        # Update weights and bias for each layer
        for layer in self.layer_list:
            # Flatten xi to ensure it's a 1D array for the outer product
            if xi.ndim > 1:
                xi = xi.flatten()

            # Update the bias
            layer.bias += np.sum(layer.y_delta, axis=0) * learning_rate

            # Update the weights using the outer product of y_delta and xi
            layer.weights += np.outer(layer.y_delta, xi) * learning_rate

            # After updating, xi becomes the output of the current layer
            xi = layer.y_delta  # This ensures xi for the next layer is correct

    def evaluate(self, evaluation_dataset):
        correct_sum = 0
        x_size = evaluation_dataset.x.shape[0]
        for i in range(x_size):
            xi = evaluation_dataset.x[i]
            yi = evaluation_dataset.y[i]
            z_list, y_predict_list = self.forward(xi)
            y_predict = y_predict_list[-1]
            y_guess = np.round(y_predict)
            # Check if the rounded prediction is correct
            if y_guess == yi:
                correct_sum += 1
            print(xi, yi, y_predict, y_guess, y_guess == yi)
        accuracy = correct_sum / x_size
        return accuracy


class BasicNetwork(NeuralNetwork):

    def __init__(self, dataset):
        super().__init__()
        self.dataset = dataset
        self.y_bias = None
        self.y_x = None
        self.layer_list = None

        self.init_network()

    def init_network(self):
        self.y_bias = np.random.normal(0, 0.5, [1, self.dataset.shape[1]])
        self.y_x = np.random.normal(0, 0.5, [self.dataset.shape[1], self.dataset.shape[0]])

    def forward(self, x):
        z = np.dot(x, self.y_x.transpose()) + self.y_bias
        y = 1 / (1 + np.exp(-z))
        return z, y

    def evaluate(self, evaluation_dataset):
        correct_sum = 0
        x_size = evaluation_dataset.x.shape[0]
        for i in range(x_size):
            xi = evaluation_dataset.x[i]
            yi = evaluation_dataset.y[i]
            z, y_predict = self.forward(xi)
            y_guess = np.round(y_predict)
            # Check if the rounded prediction is correct
            if y_guess == yi:
                correct_sum += 1
        accuracy = correct_sum / x_size
        return accuracy

    def get_gradient(self, y_predict, error):
        # Compute gradient (Sigmoid prime)
        sigmoid_prime = y_predict * (1 - y_predict)
        y_delta = error * sigmoid_prime  # Use error, not cost, for the gradient
        return y_delta

    def update(self, y_delta, xi, learning_rate):
        # Update weights and bias
        self.y_bias += np.sum(y_delta, axis=0) * learning_rate
        self.y_x += np.outer(y_delta, xi) * learning_rate

    def train(self, params, training_set, test_set):
        for epoch in range(params.num_epochs):
            cost_sum = 0
            x_size = training_set.x.shape[0]

            for i in range(x_size):
                xi = training_set.x[i]
                yi = training_set.y[i]

                # Forward pass
                z, y_predict = self.forward(xi)

                # Compute loss
                y_cost, error = self.get_loss(y_predict, yi)
                cost_sum += np.mean(y_cost)

                # Get Gradients
                y_delta = self.get_gradient(y_predict, error)

                # Update Weights
                self.update(y_delta, xi, params.learning_rate)

            if epoch % params.eval_freq == 0:
                mean_cost = cost_sum / x_size
                training_accuracy = self.evaluate(training_set)
                test_accuracy = self.evaluate(test_set)
                print(f"{epoch}\t{mean_cost:0.3f}\t{training_accuracy:0.3f}\t{test_accuracy:0.3f}")






