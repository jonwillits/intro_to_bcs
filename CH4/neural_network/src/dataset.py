import numpy as np

class Dataset:

    def __init__(self, x_range=10):
        self.x_range = x_range
        self.dataset_type = None
        self.x_labels = ['x1', 'x2']
        self.y_labels = ['y']
        self.n = None
        self.x = None
        self.y = None

    def random_dataset(self, n):
        self.dataset_type = "random"
        self.n = n
        self.y = np.array([1] * n + [0] * n)
        self.x = np.random.uniform(low=-self.x_range, high=self.x_range, size=(2 * n, 2))

    def one_d_dataset(self, n, dimension=1, noise=0.5):
        self.dataset_type = "one_d"
        self.n = n
        self.y = np.array([1] * n + [0] * n)

        # Generate base data
        random_x = np.random.uniform(low=-self.x_range, high=self.x_range, size=(2 * n, 1))
        y1_x = np.random.uniform(low=0, high=self.x_range, size=(n, 1))
        y0_x = np.random.uniform(low=-self.x_range, high=0, size=(n, 1))

        if dimension == 1:
            # Column 0 will be y1_x and y0_x, column 1 will be random_x
            self.x = np.hstack((np.vstack((y1_x, y0_x)), random_x))
        elif dimension == 2:
            # Column 0 will be random_x, column 1 will be y1_x and y0_x
            self.x = np.hstack((random_x, np.vstack((y1_x, y0_x))))
        else:
            raise ValueError('dimension must be 1 or 2')

        self.add_noise(noise)

    def generate_quadrants(self, n):
        q1 = np.random.uniform(low=-self.x_range, high=self.x_range, size=(n, 1))
        q2 = np.random.uniform(low=-self.x_range, high=self.x_range, size=(n, 1))
        q3 = np.random.uniform(low=self.x_range, high=self.x_range, size=(n, 1))
        q4 = np.random.uniform(low=self.x_range, high=self.x_range, size=(n, 1))

        return q1, q2, q3, q4

    def and_dataset(self, n, noise=0.5):
        self.dataset_type = "one_d"
        self.n = n
        self.y = np.array([1] * n + [0] * n)

        # Generate base data


        if dimension == 1:
            # Column 0 will be y1_x and y0_x, column 1 will be random_x
            self.x = np.hstack((np.vstack((y1_x, y0_x)), random_x))
        elif dimension == 2:
            # Column 0 will be random_x, column 1 will be y1_x and y0_x
            self.x = np.hstack((random_x, np.vstack((y1_x, y0_x))))
        else:
            raise ValueError('dimension must be 1 or 2')

        self.add_noise(noise)

    def add_noise(self, noise=0.5):
        # Add Gaussian noise to all values in self.x
        if self.x is None:
            raise ValueError("Dataset not generated yet. Call one_d_dataset() first.")

        noise_matrix = np.random.normal(loc=0, scale=noise, size=self.x.shape)
        self.x += noise_matrix





