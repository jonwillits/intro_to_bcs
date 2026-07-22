import numpy as np
import itertools

class Dataset:

    def __init__(self, x_size=2, dataset_type=None):
        self.dataset_name = None
        self.dataset_type = dataset_type
        self.n = None
        self.x = None
        self.y = None
        self.x_size = x_size
        self.y_size = 1

        self.init_dataset()

    def init_dataset(self):
        if isinstance(self.x_size, int) and self.x_size > 0:
            self.y_size = self.x_size
            self.generate_x_lists()
            self.generate_y_lists()
        else:
            raise Exception("ERROR, x_size must be a positive integer")

    def generate_x_lists(self):
        # Generate all possible combinations of binary values of length `x_size`
        combinations = list(itertools.product([0, 1], repeat=self.x_size))
        self.x = np.array(combinations)  # Convert to a NumPy array
        self.n = len(self.x)

    def generate_y_lists(self):
        if self.dataset_type == 'and':
            self.y = self.generate_and_y()
            self.dataset_name = "AND"
        elif self.dataset_type == 'or':
            self.y = self.generate_or_y()
            self.dataset_name = "OR"
        elif self.dataset_type == 'xor':
            self.y = self.generate_xor_y()
            self.dataset_name = "XOR"
        elif self.dataset_type == 'random':
            self.y = self.generate_random_y()
            self.dataset_name = "Random"
        elif self.dataset_type == 'x1':
            self.y = self.generate_x1_y()
            self.dataset_name = "x1"
        elif self.dataset_type == 'x2':
            self.y = self.generate_x2_y()
            self.dataset_name = "x2"
        elif self.dataset_type is None:
            self.y = self.generate_random_y()
            self.dataset_name = "Random"
        else:
            raise ValueError(f"Unknown dataset_type: {self.dataset_type}")

    def generate_and_y(self):
        # AND: Both columns should be 1 for y to be 1
        return np.where((self.x[:, 0] == 1) & (self.x[:, 1] == 1), 1, 0).reshape(-1, 1)

    def generate_or_y(self):
        # OR: At least one column should be 1 for y to be 1
        return np.where((self.x[:, 0] == 1) | (self.x[:, 1] == 1), 1, 0).reshape(-1, 1)

    def generate_xor_y(self):
        # XOR: Exactly one column should be 1 for y to be 1
        return np.where((self.x[:, 0] != self.x[:, 1]), 1, 0).reshape(-1, 1)

    def generate_random_y(self):
        # Random: Each element is randomly 0 or 1
        return np.random.randint(2, size=(self.x.shape[0], 1))

    def generate_x1_y(self):
        # Based on x1: y is equal to the value of x1
        return self.x[:, 0].reshape(-1, 1)

    def generate_x2_y(self):
        # Based on x2: y is equal to the value of x2
        return self.x[:, 1].reshape(-1, 1)
