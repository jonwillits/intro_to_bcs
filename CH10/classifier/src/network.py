import numpy as np

class Network:
    ############################################################################################################
    def __init__(self, params, input_size, output_size):

        self.input_size = input_size
        self.hidden_size = params.hidden_size
        self.output_size = output_size
        self.weight_mean = 0
        self.weight_stdev = 0.0001

        self.h_bias = None
        self.h_x = None
        self.o_bias = None
        self.o_h = None

        self.init_network()

    ############################################################################################################
    def init_network(self):

        self.h_bias = np.random.normal(0, self.weight_stdev, [self.hidden_size])
        self.h_x = np.random.normal(0, self.weight_stdev, [self.hidden_size, self.input_size])

        self.o_bias = np.random.normal(0, self.weight_stdev, [self.output_size])
        self.o_h = np.random.normal(0, self.weight_stdev, [self.output_size, self.hidden_size])

    ############################################################################################################
    def feedforward(self, x):
        h = self.tanh(np.dot(self.h_x, x) + self.h_bias)
        o = self.sigmoid(np.dot(self.o_h, h) + self.o_bias)
        return h, o

    ############################################################################################################
    @staticmethod
    def calc_cost(y, o):
        return y - o
        # absolute value of the difference

    ############################################################################################################
    def backpropogation(self, x, o, h, o_cost, learning_rate):
        o_delta = o_cost * self.sigmoid_prime(o)

        h_cost = np.dot(o_delta, self.o_h)
        h_delta = h_cost * self.tanh_prime(h)

        self.o_bias += o_delta * learning_rate
        self.o_h += (np.dot(o_delta.reshape(len(o_delta), 1), h.reshape(1, len(h))) * learning_rate)

        self.h_bias += h_delta * learning_rate
        self.h_x += (np.dot(h_delta.reshape(len(h_delta), 1), x.reshape(1, len(x))) * learning_rate)

    ############################################################################################################
    @staticmethod
    def tanh(z):
        return np.tanh(z)

    ############################################################################################################
    @staticmethod
    def tanh_prime(z):
        return 1.0 - np.tanh(z)**2

    ############################################################################################################
    @staticmethod
    def sigmoid(z):
        return 1/(1+np.exp(-z))

    ############################################################################################################
    @staticmethod
    def sigmoid_prime(z):
        return 1/(1+np.exp(-z)) * (1 - 1/(1+np.exp(-z)))
