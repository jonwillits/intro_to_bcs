import numpy as np


class NeuralNetwork:

    def __init__(self, params):
        self.input_size = params.input_size
        self.output_size = params.output_size
        self.hidden_size_list = params.hidden_size_list
        self.activation_function = params.activation_function

        self.y_bias = None
        self.y_x = None

        self.init_network()

    def init_network(self):
        self.y_bias = np.random.normal(0, 0.5, [1, self.output_size])
        self.y_x = np.random.normal(0, 0.5, [self.output_size, self.input_size])

    def net_input(self, x):
        z = np.dot(x, self.y_x.transpose()) + self.y_bias
        return z

    def forward(self, x, act_f):
        z = np.dot(x, self.y_x.transpose()) + self.y_bias
        if self.activation_function == 'Sigmoid':
            y = 1 / (1 + np.exp(-z))
        elif self.activation_function == 'Threshold':
            y = np.where(z >= 0.0, 1, 0)
        elif self.activation_function == 'Linear':
            y = z
        else:
            raise Exception(f'Activation function {self.activation_function} not supported')
        return y

    def train(self, x, y, learning_rate):

        y_predict = None
        y_cost = None
        y_delta = None

        for i in range(x.shape[0]):
            xi = x[i]
            yi = y[i]

            y_predict = self.forward(xi)
            y_cost = yi - y_predict

            if self.activation_function == 'Sigmoid':
                sigmoid_prime = 1/(1+np.exp(-y_predict)) * (1 - 1/(1+np.exp(-y_predict)))
                y_delta = y_cost * sigmoid_prime

            elif self.activation_function == 'Threshold':
                y_delta = y_cost
            elif self.activation_function == 'Linear':
                y_delta = y_cost
            else:
                raise Exception(f'Activation function {self.activation_function} not supported')

            self.y_bias += y_delta * learning_rate
            self.y_x += y_delta.transpose() * xi * learning_rate

        return y_predict, y_cost, y_delta