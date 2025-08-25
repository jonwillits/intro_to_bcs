import numpy as np


class NeuralNetwork:

    def __init__(self, params):
        self.input_size = params.input_size
        self.output_size = params.output_size
        self.hidden_size_list = params.hidden_size_list
        self.activation_function = params.activation_function
        self.learning_rate = params.learning_rate

        self.y_bias = None
        self.y_x = None

        self.init_network()

    def init_network(self):
        self.y_bias = np.random.normal(0, 0.10, [1, self.output_size])
        self.y_x = np.random.normal(0, 0.10, [self.output_size, self.input_size])

    def net_input(self, x):
        z = np.dot(x, self.y_x.transpose()) + self.y_bias
        return z

    def forward(self, x):
        z = np.dot(x, self.y_x.transpose()) + self.y_bias
        if self.activation_function == 'sigmoid':
            y = 1 / (1 + np.exp(-z))
        elif self.activation_function == 'threshold':
            y = np.where(z >= 0.0, 1, 0)
        elif self.activation_function == 'linear':
            y = z
        else:
            raise Exception(f'Activation function {self.activation_function} not supported')
        return z, y

    def train(self, x, y):

        cost_sum = 0
        output_array = np.zeros([x.shape[0]], float)

        for i in range(x.shape[0]):
            xi = x[i]
            yi = y[i]

            z, y_predict = self.forward(xi)
            y_cost = yi - y_predict
            cost_sum += y_cost
            output_array[i] = y_predict

            if self.activation_function == 'sigmoid':
                sigmoid_prime = 1/(1+np.exp(-y_predict)) * (1 - 1/(1+np.exp(-y_predict)))
                y_delta = y_cost * sigmoid_prime

            elif self.activation_function == 'threshold':
                y_delta = y_cost
            elif self.activation_function == 'linear':
                y_delta = y_cost
            else:
                raise Exception(f'Activation function {self.activation_function} not supported')

            self.y_bias += y_delta * self.learning_rate
            self.y_x += y_delta.transpose() * xi * self.learning_rate

        mean_cost = cost_sum / x.shape[0]
        rounded_output = np.round(output_array)
        y_squeezed = np.squeeze(y)
        agreement = (rounded_output == y_squeezed)
        percent_correct = np.mean(agreement)

        return output_array, rounded_output, agreement, percent_correct, mean_cost