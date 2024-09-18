import numpy as np
import copy

class NeuralNetwork:

    def __init__(self, params, dataset):
        self.input_size = dataset.shape[0]
        self.output_size = dataset.shape[1]
        self.hidden_size_list = params.hidden_size_list
        self.layer_list = None

        self.init_network()

    def __str__(self):
        output_string = "Neural Network with Layers:\n"
        if self.layer_list is not None:
            for layer in self.layer_list:
                output_string += f"\t{layer.name}: {layer.weights.shape}\n"
        return output_string

    def init_network(self):
        self.layer_list = []
        input_size = self.input_size
        if self.hidden_size_list is not None:
            for i, hidden_size in enumerate(self.hidden_size_list):
                self.layer_list.append(Layer(input_size=input_size,
                                             output_size=hidden_size,
                                             name=f'h{i+1}',
                                             activation_function='Sigmoid'))
                input_size = hidden_size

        self.layer_list.append(Layer(input_size=input_size,
                                     output_size=self.output_size,
                                     name=f'output',
                                     activation_function='Sigmoid'))

    def forward(self, x_batch):
        z = 0
        # Forward pass through all layers
        for layer in self.layer_list:
            z, x_batch = layer.forward(x_batch)

        return z, x_batch

    def train(self, params, training_set, test_set=None):

        if test_set is None:
            test_set = training_set

        x = copy.deepcopy(training_set.x)
        y = copy.deepcopy(training_set.y)

        # Shuffle the data
        indices = np.arange(x.shape[0])
        if params.shuffle_training_set:
            np.random.shuffle(indices)
        x = x[indices]
        y = y[indices]
        y_predict, cost, y_delta = None, None, None

        for epoch in range(params.num_epochs):
            for start in range(0, x.shape[0], params.batch_size):
                end = start + params.batch_size
                x_batch = x[start:end]
                y_batch = y[start:end]

                # Use the new forward method for forward pass
                z, x_batch = self.forward(x_batch)

                # Calculate the error (cost)
                y_cost = self.binary_cross_entropy(y_batch, x_batch)  # Cross-entropy loss

                # Backpropagation
                for layer in reversed(self.layer_list):
                    y_delta = layer.backpropagate_error(y_cost, z)
                    layer.update_weights(x_batch, y_delta, params.learning_rate)  # Update weights

                    # Pass the error back to the previous layer (for multi-layer networks)
                    y_cost = np.dot(y_delta, layer.weights)  # Backpropagate the error through layers

                # Optional: Compute cost for this batch if needed
                cost = np.mean(np.square(y_cost))  # Mean squared error

            if epoch % params.eval_freq == 0:
                train_percent_correct, train_loss, train_result_matrix = self.evaluate(training_set.x, training_set.y)
                test_percent_correct, test_loss, test_result_matrix = self.evaluate(test_set.x, test_set.y)
                if params.verbose:
                    np.set_printoptions(precision=3, suppress=True, linewidth=np.inf)
                    print("Training Set")
                    print(train_result_matrix)
                    print("Test Set")
                    print(test_result_matrix)
                print(f"{epoch}:\t{train_loss:0.3f}-{test_loss:0.3f}\t{train_percent_correct:0.3f}-{test_percent_correct:0.3f}")

        return y_predict, cost, y_delta

    def binary_cross_entropy(self, y_true, y_pred):
        # Add a small epsilon to prevent log(0)
        epsilon = 1e-8
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)  # Ensure y_pred is within (0,1)
        return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

    def evaluate(self, x_set, y_set):

        # Forward pass through the entire dataset
        _, y_pred = self.forward(x_set)

        # Round predictions to the nearest integer (e.g., for binary classification, this would be 0 or 1)
        y_pred_rounded = np.round(y_pred)

        # Ensure the shapes of y_pred_rounded and y_set match
        if y_pred_rounded.shape != y_set.shape:
            y_pred_rounded = y_pred_rounded.reshape(y_set.shape)

        # Compute the loss (MSE)
        total_loss = np.mean(np.square(y_set - y_pred))

        # Compute the number of correct predictions
        correct_predictions = (y_pred_rounded == y_set).astype(int)

        # Create a numpy matrix with the columns x1, x2, y, y_pred, y_pred_rounded, correct_predictions, loss
        loss_per_example = np.square(y_set - y_pred)  # Loss for each example

        # Assuming x_set has at least two input features (x1, x2)
        result_matrix = np.column_stack((
            x_set[:, 0],  # x1
            x_set[:, 1],  # x2
            y_set,  # y (true label)
            y_pred,  # y_pred (predicted output)
            y_pred_rounded,  # y_pred_rounded (rounded prediction)
            correct_predictions,  # correct_predictions (1 if correct, 0 if not)
            loss_per_example  # loss for each example
        ))

        # Percent correct (accuracy)
        percent_correct = np.sum(correct_predictions) / y_set.size * 100
        mean_loss = np.mean(loss_per_example)

        # Optionally, you can return or save the result matrices if needed
        return percent_correct, mean_loss, result_matrix,


class Layer:
    def __init__(self, input_size, output_size, name, activation_function):
        self.input_size = input_size
        self.output_size = output_size
        self.name = name
        self.activation_function = activation_function
        self.weights = None
        self.bias = None

        self.init_weights()

    def init_weights(self):
        limit = np.sqrt(6 / (self.input_size + self.output_size))
        self.weights = np.random.uniform(-limit, limit, [self.output_size, self.input_size])
        self.bias = np.random.uniform(-limit, limit, [self.output_size])

    def forward(self, x):
        z = np.dot(x, self.weights.T) + self.bias  # Pre-activation (linear transformation)
        if self.activation_function == 'Sigmoid':
            y = 1 / (1 + np.exp(-z))
        elif self.activation_function == 'Threshold':
            y = np.where(z >= 0.0, 1, 0)
        elif self.activation_function == 'Linear':
            y = z
        else:
            raise ValueError(f'Activation function {self.activation_function} not supported')

        return z, y

    def update_weights(self, x_batch, y_delta, learning_rate):
        # Update the weights based on the input x_batch and the delta (gradient of the error)
        self.weights += np.dot(y_delta.T, x_batch) * learning_rate

        # Update the biases based on the delta (sum over the batch)
        self.bias += np.sum(y_delta, axis=0) * learning_rate

    def backpropagate_error(self, y_cost, z):
        # Backpropagate the error using the derivative of the activation function
        if self.activation_function == 'Sigmoid':
            s = 1 / (1 + np.exp(-z))  # Sigmoid activation
            sigmoid_prime = s * (1 - s)
            delta = y_cost * sigmoid_prime  # Error * activation derivative
        else:
            delta = y_cost  # For linear and threshold, we just use the cost

        return delta