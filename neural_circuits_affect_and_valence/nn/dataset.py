import numpy as np
import random

class Dataset:

    def __init__(self, params):
        self.n = params.n
        self.x_range = params.x_range
        self.noise = params.noise
        self.dataset_type = None
        self.x_labels = ['x1', 'x2']
        self.y_labels = ['y']
        self.x = None
        self.y = None
        self.shape = (2, 1)

        self.generate_dataset()

    def generate_dataset(self):
        self.dataset_type = "random"
        self.y = np.array([1] * self.n + [0] * self.n)
        self.x = np.random.uniform(low=-self.x_range, high=self.x_range, size=(2 * self.n, 2))

    def add_noise(self):
        # Add Gaussian noise to all values in self.x
        if self.x is None:
            raise ValueError("Dataset not generated yet. Call one_d_dataset() first.")

        noise_matrix = np.random.normal(loc=0, scale=self.noise, size=self.x.shape)
        self.x += noise_matrix

class OneD_Dataset(Dataset):
    def __init__(self, params):
        super().__init__(params)
        self.dataset_type = "oned"

        self.generate_dataset()

    def generate_dataset(self):
        self.dataset_type = "one_d"
        self.y = np.array([1] * self.n + [0] * self.n)

        # Generate base data
        random_x = np.random.uniform(low=-self.x_range, high=self.x_range, size=(2 * self.n, 1))
        y1_x = np.random.uniform(low=0, high=self.x_range, size=(self.n, 1))
        y0_x = np.random.uniform(low=-self.x_range, high=0, size=(self.n, 1))

        dimension = random.choice([1,2])

        if dimension == 1:
            # Column 0 will be y1_x and y0_x, column 1 will be random_x
            self.x = np.hstack((np.vstack((y1_x, y0_x)), random_x))
        elif dimension == 2:
            # Column 0 will be random_x, column 1 will be y1_x and y0_x
            self.x = np.hstack((random_x, np.vstack((y1_x, y0_x))))
        else:
            raise ValueError('dimension must be 1 or 2')

        self.add_noise()

class AND_Dataset(Dataset):
    def __init__(self, params):
        super().__init__(params)
        self.dataset_type = "and"

        self.generate_dataset()

    def generate_dataset(self):

        self.y = np.array([1] * self.n + [0] * self.n)

        # Generate n points in the (+,+) quadrant
        x1_pos = np.random.uniform(0, self.x_range, self.n)
        x2_pos = np.random.uniform(0, self.x_range, self.n)
        points_pos = np.vstack((x1_pos, x2_pos)).T

        # Divide the remaining n points evenly into the other three quadrants
        n_third = self.n // 3
        remainder = self.n % 3

        # Generate n/3 points for each of the other quadrants
        x1_neg_pos = np.random.uniform(-self.x_range, 0, n_third)  # (-,+)
        x2_neg_pos = np.random.uniform(0, self.x_range, n_third)

        x1_pos_neg = np.random.uniform(0, self.x_range, n_third)  # (+,-)
        x2_pos_neg = np.random.uniform(-self.x_range, 0, n_third)

        x1_neg = np.random.uniform(-self.x_range, 0, n_third + remainder)  # (-,-), include remainder here
        x2_neg = np.random.uniform(-self.x_range, 0, n_third + remainder)

        # Stack the points for the other quadrants
        points_other_quadrants = np.vstack((
            np.vstack((x1_neg_pos, x2_neg_pos)).T,
            np.vstack((x1_pos_neg, x2_pos_neg)).T,
            np.vstack((x1_neg, x2_neg)).T
        ))

        # Concatenate the (+,+) points with the other quadrant points
        self.x = np.vstack((points_pos, points_other_quadrants))

        self.add_noise()

class OR_Dataset(Dataset):

    def __init__(self, params):
        super().__init__(params)
        self.dataset_type = "or"

        self.generate_dataset()

    def generate_dataset(self):
        self.y = np.array([1] * self.n + [0] * self.n)

        # Divide n into thirds for the (+,+), (+,-), and (-,+) quadrants
        n_third = self.n // 3
        remainder = self.n % 3

        # Generate n/3 points for each of the (+,+), (+,-), and (-,+) quadrants
        x1_pos_pos = np.random.uniform(0, self.x_range, n_third)  # (+,+)
        x2_pos_pos = np.random.uniform(0, self.x_range, n_third)

        x1_pos_neg = np.random.uniform(0, self.x_range, n_third)  # (+,-)
        x2_pos_neg = np.random.uniform(-self.x_range, 0, n_third)

        x1_neg_pos = np.random.uniform(-self.x_range, 0, n_third + remainder)  # (-,+)
        x2_neg_pos = np.random.uniform(0, self.x_range, n_third + remainder)

        # Generate n points for the (-,-) quadrant
        x1_neg_neg = np.random.uniform(-self.x_range, 0, self.n)
        x2_neg_neg = np.random.uniform(-self.x_range, 0, self.n)

        # Stack the points for the (+,+), (+,-), and (-,+) quadrants
        points_or_quadrants = np.vstack((
            np.vstack((x1_pos_pos, x2_pos_pos)).T,
            np.vstack((x1_pos_neg, x2_pos_neg)).T,
            np.vstack((x1_neg_pos, x2_neg_pos)).T
        ))

        # Stack the points for the (-,-) quadrant
        points_neg_neg = np.vstack((x1_neg_neg, x2_neg_neg)).T

        # Concatenate the points from the "or" quadrants and the (-,-) quadrant
        self.x = np.vstack((points_or_quadrants, points_neg_neg))

        self.add_noise()

class XOR_Dataset(Dataset):

    def __init__(self, params):
        super().__init__(params)
        self.dataset_type = "xor"

        self.generate_dataset()

    def generate_dataset(self):
        self.y = np.array([1] * self.n + [0] * self.n)

        # Divide n into half for y=0 and y=1 points
        n_half = self.n // 2
        remainder = self.n % 2

        # Generate points for y=0:
        # First half in (-category_mean, -category_mean) quadrant
        x1_neg_neg = np.random.uniform(-self.x_range, 0, n_half)  # (-,-)
        x2_neg_neg = np.random.uniform(-self.x_range, 0, n_half)

        # Second half (including remainder) in (category_mean, category_mean) quadrant
        x1_pos_pos = np.random.uniform(0, self.x_range, n_half + remainder)  # (+,+)
        x2_pos_pos = np.random.uniform(0, self.x_range, n_half + remainder)

        # Generate points for y=1:
        # First half in (-category_mean, category_mean) quadrant
        x1_neg_pos = np.random.uniform(-self.x_range, 0, n_half)  # (-,+)
        x2_neg_pos = np.random.uniform(0, self.x_range, n_half)

        # Second half (including remainder) in (category_mean, -category_mean) quadrant
        x1_pos_neg = np.random.uniform(0, self.x_range, n_half + remainder)  # (+,-)
        x2_pos_neg = np.random.uniform(-self.x_range, 0, n_half + remainder)

        # Stack the points for y=0
        points_y0 = np.vstack((
            np.vstack((x1_neg_neg, x2_neg_neg)).T,
            np.vstack((x1_pos_pos, x2_pos_pos)).T
        ))

        # Stack the points for y=1
        points_y1 = np.vstack((
            np.vstack((x1_neg_pos, x2_neg_pos)).T,
            np.vstack((x1_pos_neg, x2_pos_neg)).T
        ))

        # Concatenate the points for y=0 and y=1
        self.x = np.vstack((points_y1, points_y0))

        self.add_noise()

class SpiralDataset(Dataset):
    def __init__(self, params):
        super().__init__(params)
        self.dataset_type = "spiral"

        self.generate_dataset()

    def generate_spiral(self, n, delta_t, label, noise):
        # Initialize arrays for x1, x2, and labels
        x1 = np.zeros(n)
        x2 = np.zeros(n)
        y = np.full(n, label)

        for i in range(n):
            r = i / n * 5  # Scaling factor for radius
            t = 1.75 * i / n * 2 * np.pi + delta_t  # Angular position with offset
            x1[i] = r * np.sin(t) + np.random.uniform(-1, 1) * noise  # Add noise to x-coordinate
            x2[i] = r * np.cos(t) + np.random.uniform(-1, 1) * noise  # Add noise to y-coordinate

        return x1, x2, y

    def generate_dataset(self):
        # Generate y=1 examples with deltaT=0
        x1_y1, x2_y1, y_y1 = self.generate_spiral(self.n, 0, 1, self.noise)

        # Generate y=0 examples with deltaT=Math.PI
        x1_y0, x2_y0, y_y0 = self.generate_spiral(self.n, np.pi, 0, self.noise)

        # Combine the points and labels
        self.x = np.vstack((np.hstack((x1_y1, x1_y0)), np.hstack((x2_y1, x2_y0)))).T
        self.y = np.hstack((y_y1, y_y0))

class CircleDataset(Dataset):
    def __init__(self, params):
        self.radius = params.radius
        super().__init__(params)
        self.dataset_type = "circle"

        self.generate_dataset()

    def get_circle_label(self, p, center, radius):
        dist = np.sqrt((p[0] - center[0]) ** 2 + (p[1] - center[1]) ** 2)
        return 1 if dist < (radius * 0.5) else 0

    def generate_dataset(self):
        # Initialize the array for points and labels
        self.x = np.zeros((self.n, 2))
        self.y = np.zeros(self.n)

        center = (0, 0)

        # Generate positive points inside the circle (y=1)
        for i in range(self.n // 2):
            r = np.random.uniform(0, self.radius * 0.5)
            angle = np.random.uniform(0, 2 * np.pi)
            x = r * np.sin(angle)
            y = r * np.cos(angle)
            noise_x = np.random.uniform(-self.radius, self.radius) * self.noise
            noise_y = np.random.uniform(-self.radius, self.radius) * self.noise
            self.x[i, 0] = x + noise_x
            self.x[i, 1] = y + noise_y
            self.y[i] = self.get_circle_label((self.x[i, 0], self.x[i, 1]), center, self.radius)

        # Generate negative points outside the circle (y=0)
        for i in range(self.n // 2, self.n):
            r = np.random.uniform(self.radius * 0.7, self.radius)
            angle = np.random.uniform(0, 2 * np.pi)
            x = r * np.sin(angle)
            y = r * np.cos(angle)
            noise_x = np.random.uniform(-self.radius, self.radius) * self.noise
            noise_y = np.random.uniform(-self.radius, self.radius) * self.noise
            self.x[i, 0] = x + noise_x
            self.x[i, 1] = y + noise_y
            self.y[i] = self.get_circle_label((self.x[i, 0], self.x[i, 1]), center, self.radius)

def generate_dataset(params):
    if params.dataset_type == 'one_d':
        training_set = OneD_Dataset(params)
        test_set = OneD_Dataset(params)
    elif params.dataset_type == 'and':
        training_set = AND_Dataset(params)
        test_set = AND_Dataset(params)
    elif params.dataset_type == 'or':
        training_set = OR_Dataset(params)
        test_set = OR_Dataset(params)
    elif params.dataset_type == 'xor':
        training_set = XOR_Dataset(params)
        test_set = XOR_Dataset(params)
    elif params.dataset_type == 'circle':
        training_set = CircleDataset(params)
        test_set = CircleDataset(params)
    elif params.dataset_type == 'spiral':
        training_set = SpiralDataset(params)
        test_set = SpiralDataset(params)
    else:
        training_set = Dataset(params)
        test_set = Dataset(params)

    return training_set, test_set






