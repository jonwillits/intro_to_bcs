from src import dataset
from src import visualizations

#
# def rand_uniform(low, high, size=1):
#     return np.random.uniform(low, high, size)
#
#
# def gen_spiral(n, delta_t, label, noise):
#     points = []
#     for i in range(n):
#         r = i / n * 5  # Scaling factor for radius
#         t = 1.75 * i / n * 2 * np.pi + delta_t  # Angular position with offset
#         x = r * np.sin(t) + rand_uniform(-1, 1) * noise  # Add noise to x-coordinate
#         y = r * np.cos(t) + rand_uniform(-1, 1) * noise  # Add noise to y-coordinate
#         points.append({'x1': x, 'x2': y, 'y': label})
#     return points
#
#
# def generate_spiral_dataset(n, noise=.1):
#     # Generate y=1 examples with deltaT=0
#     points_y1 = gen_spiral(n, 0, 1, noise)
#
#     # Generate y=0 examples with deltaT=Math.PI
#     points_y0 = gen_spiral(n, np.pi, 0, noise)
#
#     # Combine the points
#     points = points_y1 + points_y0
#
#     # Convert to a DataFrame
#     df = pd.DataFrame(points)
#     return df
#
#
# def get_circle_label(p, center, radius):
#     dist = np.sqrt((p[0] - center[0]) ** 2 + (p[1] - center[1]) ** 2)
#     return 1 if dist < (radius * 0.5) else 0
#
# def generate_circle_dataset(n, noise, radius=5):
#     points = []
#     center = (0, 0)
#
#     # Generate positive points inside the circle.
#     for i in range(n // 2):
#         r = rand_uniform(0, radius * 0.5)[0]
#         angle = rand_uniform(0, 2 * np.pi)[0]
#         x = r * np.sin(angle)
#         y = r * np.cos(angle)
#         noise_x = rand_uniform(-radius, radius)[0] * noise
#         noise_y = rand_uniform(-radius, radius)[0] * noise
#         label = get_circle_label((x + noise_x, y + noise_y), center, radius)
#         points.append({'x1': x + noise_x, 'x2': y + noise_y, 'y': label})
#
#     # Generate negative points outside the circle.
#     for i in range(n // 2):
#         r = rand_uniform(radius * 0.7, radius)[0]
#         angle = rand_uniform(0, 2 * np.pi)[0]
#         x = r * np.sin(angle)
#         y = r * np.cos(angle)
#         noise_x = rand_uniform(-radius, radius)[0] * noise
#         noise_y = rand_uniform(-radius, radius)[0] * noise
#         label = get_circle_label((x + noise_x, y + noise_y), center, radius)
#         points.append({'x1': x + noise_x, 'x2': y + noise_y, 'y': label})
#
#     # Convert to DataFrame
#     data = pd.DataFrame(points)
#     return data
#
#
# def generate_xor_dataset(n, category_mean, category_stdev):
#     # Generate n values for y=1 and n values for y=0
#     y = np.array([1] * n + [0] * n)
#
#     # Initialize x1 and x2 arrays of size 2*n
#     x1 = np.zeros(2 * n).astype(int)
#     x2 = np.zeros(2 * n).astype(int)
#
#     # Get the indices of the y=1 values
#     y1_indices = np.where(y == 1)[0]
#
#     # Divide y=1 points into two groups
#     n_half = n // 2
#     remainder = n % 2
#
#     # First half: x1 ~ N(-category_mean, category_stdev), x2 ~ N(category_mean, category_stdev)
#     x1[y1_indices[:n_half]] = np.random.normal(-category_mean, category_stdev, n_half).astype(int)
#     x2[y1_indices[:n_half]] = np.random.normal(category_mean, category_stdev, n_half).astype(int)
#
#     # Second half (including remainder): x1 ~ N(category_mean, category_stdev), x2 ~ N(-category_mean, category_stdev)
#     x1[y1_indices[n_half:]] = np.random.normal(category_mean, category_stdev, n_half + remainder).astype(int)
#     x2[y1_indices[n_half:]] = np.random.normal(-category_mean, category_stdev, n_half + remainder).astype(int)
#
#     # Get the indices of the y=0 values
#     y0_indices = np.where(y == 0)[0]
#
#     # First half: x1 ~ N(-category_mean, category_stdev), x2 ~ N(-category_mean, category_stdev)
#     x1[y0_indices[:n_half]] = np.random.normal(-category_mean, category_stdev, n_half).astype(int)
#     x2[y0_indices[:n_half]] = np.random.normal(-category_mean, category_stdev, n_half).astype(int)
#
#     # Second half (including remainder): x1 ~ N(category_mean, category_stdev), x2 ~ N(category_mean, category_stdev)
#     x1[y0_indices[n_half:]] = np.random.normal(category_mean, category_stdev, n_half + remainder).astype(int)
#     x2[y0_indices[n_half:]] = np.random.normal(category_mean, category_stdev, n_half + remainder).astype(int)
#
#     # Create a DataFrame
#     data = pd.DataFrame({
#         'x1': x1,
#         'x2': x2,
#         'y': y
#     })
#
#     return data
#
#
# def generate_or_dataset(n, category_mean, category_stdev):
#     # Generate n values for y=1 and n values for y=0
#     y = np.array([1] * n + [0] * n)
#
#     # Initialize x1 and x2 arrays of size 2*n
#     x1 = np.zeros(2 * n).astype(int)
#     x2 = np.zeros(2 * n).astype(int)
#
#     # Get the indices of the y=1 values
#     y1_indices = np.where(y == 1)[0]
#
#     # Divide y=1 points into thirds
#     n_third = n // 3
#     remainder = n % 3
#
#     # First third: x1 ~ N(category_mean, category_stdev), x2 ~ N(category_mean, category_stdev)
#     x1[y1_indices[:n_third]] = np.random.normal(category_mean, category_stdev, n_third).astype(int)
#     x2[y1_indices[:n_third]] = np.random.normal(category_mean, category_stdev, n_third).astype(int)
#
#     # Second third: x1 ~ N(-category_mean, category_stdev), x2 ~ N(category_mean, category_stdev)
#     x1[y1_indices[n_third:2*n_third]] = np.random.normal(-category_mean, category_stdev, n_third).astype(int)
#     x2[y1_indices[n_third:2*n_third]] = np.random.normal(category_mean, category_stdev, n_third).astype(int)
#
#     # Final third (including remainder): x1 ~ N(category_mean, category_stdev), x2 ~ N(-category_mean, category_stdev)
#     x1[y1_indices[2*n_third:]] = np.random.normal(category_mean, category_stdev, n_third + remainder).astype(int)
#     x2[y1_indices[2*n_third:]] = np.random.normal(-category_mean, category_stdev, n_third + remainder).astype(int)
#
#     # Get the indices of the y=0 values
#     y0_indices = np.where(y == 0)[0]
#
#     # For y=0, all points come from (-category_mean, -category_mean) quadrant
#     x1[y0_indices] = np.random.normal(-category_mean, category_stdev, n).astype(int)
#     x2[y0_indices] = np.random.normal(-category_mean, category_stdev, n).astype(int)
#
#     # Create a DataFrame
#     data = pd.DataFrame({
#         'x1': x1,
#         'x2': x2,
#         'y': y
#     })
#
#     return data
#
#
#
# def generate_and_dataset(n, category_mean, category_stdev):
#     # Generate n values for y=1 and n values for y=0
#     y = np.array([1] * n + [0] * n)
#
#     # Generate group1 (mean=category_mean, stdev=category_stdev) for y=1
#     group1_x1 = np.random.normal(category_mean, category_stdev, n).astype(int)
#     group1_x2 = np.random.normal(category_mean, category_stdev, n).astype(int)
#
#     # Initialize x1 and x2 arrays of size 2*n
#     x1 = np.zeros(2 * n).astype(int)
#     x2 = np.zeros(2 * n).astype(int)
#
#     # For y=1, assign x1 and x2 using group1 values
#     x1[y == 1] = group1_x1
#     x2[y == 1] = group1_x2
#
#     # Get the indices of the y=0 values
#     y0_indices = np.where(y == 0)[0]
#
#     # Divide y=0 points into thirds
#     n_third = n // 3
#     remainder = n % 3
#
#     # First third: x1 ~ N(category_mean, category_stdev), x2 ~ N(-category_mean, category_stdev)
#     x1[y0_indices[:n_third]] = np.random.normal(category_mean, category_stdev, n_third).astype(int)
#     x2[y0_indices[:n_third]] = np.random.normal(-category_mean, category_stdev, n_third).astype(int)
#
#     # Second third: x1 ~ N(-category_mean, category_stdev), x2 ~ N(category_mean, category_stdev)
#     x1[y0_indices[n_third:2*n_third]] = np.random.normal(-category_mean, category_stdev, n_third).astype(int)
#     x2[y0_indices[n_third:2*n_third]] = np.random.normal(category_mean, category_stdev, n_third).astype(int)
#
#     # Final third: x1 ~ N(-category_mean, category_stdev), x2 ~ N(-category_mean, category_stdev)
#     x1[y0_indices[2*n_third:]] = np.random.normal(-category_mean, category_stdev, n_third + remainder).astype(int)
#     x2[y0_indices[2*n_third:]] = np.random.normal(-category_mean, category_stdev, n_third + remainder).astype(int)
#
#     # Create a DataFrame
#     data = pd.DataFrame({
#         'x1': x1,
#         'x2': x2,
#         'y': y
#     })
#
#     return data
#
#
# def generate_x_dataset(n, dimension, category_mean, category_stdev, random_mean, random_stdev):
#     # Generate n values for y=1 and n values for y=0
#     y = np.array([1] * n + [0] * n)
#
#     # Generate random values for the non-specified dimension (mean=0, stdev=3)
#     random = np.random.normal(random_mean, random_stdev, 2 * n).astype(int)
#
#     # Generate group1 (mean=3, stdev=3) and group2 (mean=-3, stdev=3) for the specified dimension
#     group1 = np.random.normal(category_mean, category_stdev, n).astype(int)
#     group2 = np.random.normal(-category_mean, category_stdev, n).astype(int)
#
#     if dimension == 1:
#         # Assign group1 and group2 to x1 based on y, and random to x2
#         x1 = np.where(y == 1, np.tile(group1, int(len(y) / n)), np.tile(group2, int(len(y) / n)))
#         x2 = random
#     elif dimension == 2:
#         # Assign group1 and group2 to x2 based on y, and random to x1
#         x1 = random
#         x2 = np.where(y == 1, np.tile(group1, int(len(y) / n)), np.tile(group2, int(len(y) / n)))
#     else:
#         raise ValueError(f"Dimension '{dimension}' not recognized. It should be either 1 or 2.")
#
#     # Create a DataFrame
#     data = pd.DataFrame({
#         'x1': x1,
#         'x2': x2,
#         'y': y
#     })
#
#     return data
#
#
#
# def generate_dataset(n, category_type="random", category_mean=3, category_stdev=3, random_mean=0, random_stdev=3,
#                      radius=5, noise=0.1):
#     if category_type == "random":
#         return generate_random_dataset(n, random_mean, random_stdev)
#     elif category_type == "x1":
#         return generate_x_dataset(n, 1, category_mean, category_stdev, random_mean, random_stdev)
#     elif category_type == "x2":
#         return generate_x_dataset(n, 2, category_mean, category_stdev, random_mean, random_stdev)
#     elif category_type == "and":
#         return generate_and_dataset(n, category_mean, category_stdev)
#     elif category_type == "or":
#         return generate_or_dataset(n, category_mean, category_stdev)
#     elif category_type == "xor":
#         return generate_xor_dataset(n, category_mean, category_stdev)
#     elif category_type == "circle":
#         return generate_circle_dataset(n, noise, radius)
#     elif category_type == "spiral":
#         return generate_spiral_dataset(n, noise)
#     else:
#         raise ValueError(f"Category type '{category_type}' not recognized.")
#

def generate_dataset(dataset_type, n, noise):
    training_set = dataset.Dataset()
    test_set = dataset.Dataset()

    if dataset_type == 'one_d':
        training_set.one_d_dataset(n, noise=noise)
        test_set.one_d_dataset(n, noise=noise)
    else:
        training_set.random_dataset(n)
        test_set.random_dataset(n)

    return training_set, test_set

def main():
    n = 200
    noise = 1
    dataset_type = "one_d"

    training_set, test_set = generate_dataset(dataset_type, n, noise)
    visualizations.plot_dataset(training_set, test_set)

if __name__ == "__main__":
    main()
