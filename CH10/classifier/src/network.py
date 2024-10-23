import numpy as np


class Network:

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

    def init_network(self):
        # Xavier initialization for hidden weights
        limit_h_x = np.sqrt(6 / (self.input_size + self.hidden_size))
        self.h_x = np.random.uniform(-limit_h_x, limit_h_x, (self.hidden_size, self.input_size))
        self.h_bias = np.zeros(self.hidden_size) + 0.01

        # Xavier initialization for output weights
        limit_o_h = np.sqrt(6 / (self.hidden_size + self.output_size))
        self.o_h = np.random.uniform(-limit_o_h, limit_o_h, (self.output_size, self.hidden_size))
        self.o_bias = np.zeros(self.output_size) + 0.01

    def forward(self, x):
        h = self.tanh(np.dot(self.h_x, x) + self.h_bias)
        o = self.sigmoid(np.dot(self.o_h, h) + self.o_bias)
        return h, o

    @staticmethod
    def calc_cost(y, o):
        epsilon = 1e-12
        o = np.clip(o, epsilon, 1. - epsilon)
        return -np.mean(y * np.log(o) + (1 - y) * np.log(1 - o))

    def backpropagation(self, x, o, h, y, learning_rate):
        o_delta = o - y  # Cross-entropy gradient for output layer

        h_cost = np.dot(o_delta, self.o_h)
        h_delta = h_cost * self.tanh_prime(h)

        self.o_bias -= o_delta * learning_rate
        self.o_h -= np.dot(o_delta.reshape(len(o_delta), 1), h.reshape(1, len(h))) * learning_rate

        self.h_bias -= h_delta * learning_rate
        self.h_x -= np.dot(h_delta.reshape(len(h_delta), 1), x.reshape(1, len(x))) * learning_rate

    @staticmethod
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))

    @staticmethod
    def tanh(z):
        return np.tanh(z)

    @staticmethod
    def tanh_prime(a):
        return 1 - a ** 2
