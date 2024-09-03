import math
import random


def get_distribution_xys(mean, stdev):
    # Generate x values (centered around the mean)
    min_value = mean - 4 * stdev
    max_value = mean + 4 * stdev

    x_values = values = [x for x in range(int(min_value), int(max_value) + 1, 1)]
    y_values = []

    # Calculate y values using the normal distribution formula
    for x in x_values:
        y = get_y_at_x(mean, stdev, x)
        y_values.append(y)

    return x_values, y_values


def get_y_at_x(mean, stdev, x):
    exponent = -((x - mean) ** 2) / (2 * (stdev ** 2))
    y = (1 / (stdev * math.sqrt(2 * math.pi))) * math.exp(exponent)
    return y


def get_sample(mean, stdev, sample_size):
    sample_list = []
    for i in range(sample_size):
        value = random.gauss(mean, stdev)
        sample_list.append(value)
    return sample_list


def estimate_area_below(x, mean, stdev, num_points=1000):
    """Estimate the area under the normal distribution curve below a given x value."""
    min_x = mean - 5 * stdev  # Start far enough left to approximate the entire curve
    max_x = x  # End at the given x value
    step = (max_x - min_x) / num_points

    area = 0.0
    for i in range(num_points):
        x0 = min_x + i * step
        x1 = min_x + (i + 1) * step
        y0 = get_y_at_x(x0, mean, stdev)
        y1 = get_y_at_x(x1, mean, stdev)
        # Trapezoidal rule: average the heights of the two adjacent points and multiply by the step width
        area += (y0 + y1) * step / 2

    return area