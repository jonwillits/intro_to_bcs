import random
import math
import numpy as np

class Shapes:

    # Hardcoded default values
    instances_per_category = 10
    noise = 0.1
    image_size = 32
    category_list = ['triangle', 'rectangle', 'square', 'rhombus', 'trapezoid',
                     'pentagon', 'hexagon', 'circle', 'oval', 'star']

    def __init__(self, params):
        # Access the params.Shapes class for parameter values, and use defaults if not present
        self.image_size = getattr(params, 'image_size', Shapes.image_size)
        self.instances_per_category = getattr(params, 'instances_per_category', Shapes.instances_per_category)
        self.noise = getattr(params, 'noise', Shapes.noise)
        self.category_list = getattr(params, 'category_list', Shapes.category_list)

        # Initialize data storage for x and y coordinates
        self.x_list = []
        self.y_list = []
        self.dataset_size = None

        # Initialize categories
        self.category_index_list = {item: index for index, item in enumerate(self.category_list)}
        self.num_categories = len(self.category_list)

        # Generate the dataset
        self.generate_dataset()

    def generate_dataset(self):
        for category in self.category_list:
            if category == "circle":
                self.generate_circle_instances()
            elif category == "oval":
                self.generate_oval_instances()
            else:
                self.generate_polygon_instances(category)
        self.dataset_size = len(self.x_list)

    def print_shape(self, instance):
        image_2d = instance.reshape((self.image_size, self.image_size))
        for row in image_2d:
            line = ' '.join('O' if pixel > 0 else '.' for pixel in row)
            print(line)

    def add_noise(self):
        """
        Adds noise to each image in x_list.
        - Pixels with value 1 have a probability of self.noise to flip to 0.
        - Pixels with value 0 have a probability of self.noise * 0.1 to flip to 1.
        """
        for i in range(len(self.x_list)):
            noisy_image = self.x_list[i].copy()  # Copy the original image to avoid modifying in-place

            for j in range(len(noisy_image)):
                pixel = noisy_image[j]

                if pixel == 1.0:
                    # With probability self.noise, change 1 to 0
                    if random.random() < self.noise:
                        noisy_image[j] = 0.0

                elif pixel == 0.0:
                    # With probability self.noise * 0.1, change 0 to 1
                    if random.random() < self.noise * 0.1:
                        noisy_image[j] = 1.0

            # Replace the original image with the noisy image in x_list
            self.x_list[i] = noisy_image

    @staticmethod
    def draw_line(image, x1, y1, x2, y2, thickness=1):
        """
        Draw a line from (x1, y1) to (x2, y2) on a 2D image using Bresenham's line algorithm.
        Optionally apply a thickness to the line.
        """
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            # Set the pixel for the current point, apply thickness if needed
            for i in range(-thickness // 2, thickness // 2 + 1):
                for j in range(-thickness // 2, thickness // 2 + 1):
                    if 0 <= x1 + i < image.shape[0] and 0 <= y1 + j < image.shape[1]:
                        image[x1 + i, y1 + j] = 1.0

            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    def generate_circle_instances(self):
        for _ in range(self.instances_per_category):
            # Generate a random diameter between min_d and image_size - 1
            diameter = random.randint(5, self.image_size - 1)
            radius = diameter // 2

            # Create a blank image of zeros (2D numpy array of shape image_size x image_size)
            image = np.zeros((self.image_size, self.image_size), dtype=np.float32)

            # Randomly choose the center of the circle, ensuring it stays within bounds
            center_x = random.randint(radius, self.image_size - radius)
            center_y = random.randint(radius, self.image_size - radius)

            # Define a base tolerance that scales with the radius, and a randomization factor
            base_tolerance = radius * .5  # e.g., 10% of the radius
            randomization_factor = 0.5  # Allow for +/- 0.5 random variation

            # Draw the circle outline by setting the pixels near the perimeter to 1
            for x in range(self.image_size):
                for y in range(self.image_size):
                    # Calculate the distance from the center
                    distance_to_center = (x - center_x) ** 2 + (y - center_y) ** 2
                    # Randomize the tolerance for this pixel
                    tolerance = base_tolerance + random.uniform(-randomization_factor, randomization_factor)
                    if abs(distance_to_center - radius ** 2) <= tolerance ** 2:
                        image[x, y] = 1.0  # Mark the pixel as part of the outline

            # Flatten the image to a 1D array and append to x_list
            self.x_list.append(image.flatten())

            # Append the category index for "circle" to y_list
            self.y_list.append(self.category_index_list['circle'])

    def generate_oval_instances(self):
        for _ in range(self.instances_per_category):
            # Random semi-major and semi-minor axes with a minimum size
            major_axis = random.randint(max(10, self.image_size // 5), self.image_size - 1)
            minor_axis = random.randint(max(5, major_axis // 2), major_axis - 2)  # Ensure distinct axes

            # Ensure a significant difference between major and minor axis to avoid near-circles
            while major_axis - minor_axis < 5:
                minor_axis = random.randint(max(5, major_axis // 2), major_axis - 2)

            # Random rotation angle (in radians), avoid values too close to 0 or 2π
            theta = random.uniform(0.1, 2 * math.pi - 0.1)

            # Create a blank image of zeros (2D numpy array of shape image_size x image_size)
            image = np.zeros((self.image_size, self.image_size), dtype=np.float32)

            # Randomly choose the center of the oval, ensuring it stays within a safer buffer range
            buffer_x = min(major_axis // 2 + 5, self.image_size // 2)  # Clamp buffer_x to be within image bounds
            buffer_y = min(minor_axis // 2 + 5, self.image_size // 2)  # Clamp buffer_y to be within image bounds

            center_x = random.randint(buffer_x, self.image_size - buffer_x)
            center_y = random.randint(buffer_y, self.image_size - buffer_y)

            # Define a base tolerance that scales with the major/minor axis, and a randomization factor
            base_tolerance = 0.02 * min(major_axis, minor_axis)
            randomization_factor = 0.2  # Allow for +/- variation

            # Draw the oval outline by setting the pixels near the perimeter to 1
            for x in range(self.image_size):
                for y in range(self.image_size):
                    # Apply rotation to coordinates
                    x_prime = (x - center_x) * math.cos(theta) + (y - center_y) * math.sin(theta)
                    y_prime = -(x - center_x) * math.sin(theta) + (y - center_y) * math.cos(theta)

                    # Calculate the distance for the oval equation
                    distance_to_oval = (x_prime ** 2) / (major_axis // 2) ** 2 + (y_prime ** 2) / (minor_axis // 2) ** 2

                    # Randomize the tolerance for this pixel
                    tolerance = base_tolerance + random.uniform(-randomization_factor, randomization_factor)

                    # Check if the point is on the outline (i.e., distance_to_oval ≈ 1)
                    if abs(distance_to_oval - 1) <= tolerance:
                        image[x, y] = 1.0  # Mark the pixel as part of the outline

            # Flatten the image to a 1D array and append to x_list
            self.x_list.append(image.flatten())

            # Append the category index for "oval" to y_list
            self.y_list.append(self.category_index_list['oval'])

    def generate_polygon_instances(self, shape):
        for _ in range(self.instances_per_category):
            # Get the points for the shape
            points = self.generate_points_for_shape(shape)

            if points is not None:
                # Scale, rotate, and translate the points
                points = self.scale_points(points, self.image_size)
                points = self.rotate_points(points)
                points = self.translate_points(points, self.image_size)

                # Create a blank image of zeros
                image = np.zeros((self.image_size, self.image_size), dtype=np.float32)

                # Generate a random thickness for the entire shape
                thickness = random.choice([0, 0, 1, 1, 1, 2, 3])

                # Draw the polygon with the generated points and uniform thickness
                self.draw_shape(image, points, thickness)

                # Flatten the image to a 1D array and append to x_list
                self.x_list.append(image.flatten())

                # Append the category index for the shape to y_list
                self.y_list.append(self.category_index_list[shape])

    def generate_points_for_shape(self, shape):
        """Generate the base points for a given shape."""
        if shape == "triangle":
            return self.generate_polygon_points(3)
        elif shape == "square":
            return self.generate_polygon_points(4)
        elif shape == "pentagon":
            return self.generate_polygon_points(5)
        elif shape == "hexagon":
            return self.generate_polygon_points(6)
        elif shape == "rectangle":
            return self.generate_rectangle_points()
        elif shape == "trapezoid":
            return self.generate_trapezoid_points()
        elif shape == "rhombus":
            return self.generate_rhombus_points()
        elif shape == "star":
            return self.generate_star_points()
        else:
            raise NotImplementedError(f"Shape {shape} not implemented")

    @staticmethod
    def generate_polygon_points(n_sides):
        """Generate the base points for a regular n-sided polygon centered at the origin."""
        points = []
        angle_between_vertices = 2 * np.pi / n_sides  # Angle between vertices in radians

        # Generate the points for the polygon
        for i in range(n_sides):
            angle = i * angle_between_vertices
            x = np.cos(angle)  # x coordinate
            y = np.sin(angle)  # y coordinate
            points.append(np.array([x, y]))

        return points

    @staticmethod
    def generate_rectangle_points():
        """Generate points for a rectangle centered at the origin with random side lengths."""
        width_scale = random.uniform(0.5, 1.5)
        height_scale = random.uniform(0.5, 1.5)

        p1 = np.array([-1.0 * width_scale, 1.0 * height_scale])  # Top left
        p2 = np.array([1.0 * width_scale, 1.0 * height_scale])  # Top right
        p3 = np.array([1.0 * width_scale, -1.0 * height_scale])  # Bottom right
        p4 = np.array([-1.0 * width_scale, -1.0 * height_scale])  # Bottom left
        return [p1, p2, p3, p4]

    @staticmethod
    def generate_trapezoid_points():
        """Generate points for a trapezoid centered at the origin."""
        top_width = random.uniform(0.5, 1.0)
        bottom_width = random.uniform(1.0, 1.5)
        height = random.uniform(0.5, 1.0)

        p1 = np.array([-top_width, height])  # Top left
        p2 = np.array([top_width, height])  # Top right
        p3 = np.array([bottom_width, -height])  # Bottom right
        p4 = np.array([-bottom_width, -height])  # Bottom left
        return [p1, p2, p3, p4]

    @staticmethod
    def generate_rhombus_points():
        """Generate points for a rhombus centered at the origin."""
        d1 = random.uniform(0.5, 1.5)  # Diagonal 1 length
        d2 = random.uniform(0.5, 1.5)  # Diagonal 2 length

        p1 = np.array([0.0, d1])  # Top vertex
        p2 = np.array([d2, 0.0])  # Right vertex
        p3 = np.array([0.0, -d1])  # Bottom vertex
        p4 = np.array([-d2, 0.0])  # Left vertex
        return [p1, p2, p3, p4]

    @staticmethod
    def generate_star_points():
        """Generate the base star points with 4, 5, or 6 arms centered at the origin."""
        # Randomly choose the number of arms (points) for the star
        num_arms = random.choice([4, 5, 6])

        # Angles between points (both inner and outer)
        num_vertices = num_arms * 2  # Each arm has 2 points (inner and outer)
        angle_between_vertices = 2 * np.pi / num_vertices

        # Set radii for inner and outer points
        inner_radius = random.uniform(0.3, 0.6)  # Smaller inner radius
        outer_radius = 1.0  # Outer radius, scaling factor to ensure outer points are larger

        # Generate the points alternating between inner and outer radii
        points = []
        for i in range(num_vertices):
            angle = i * angle_between_vertices
            radius = outer_radius if i % 2 == 0 else inner_radius  # Alternate radii
            x = np.cos(angle) * radius
            y = np.sin(angle) * radius
            points.append(np.array([x, y]))

        return points

    @staticmethod
    def scale_points(points, image_size):
        """Scale the points based on a random size scaling factor."""
        # Adjust scaling to make sure the shapes are not too big
        max_scale_factor = 0.8  # Max 80% of the image size, to leave some padding
        scale = random.uniform(0.3, max_scale_factor)  # Reduced range for more control
        return [p * image_size // 2 * scale for p in points]

    @staticmethod
    def rotate_points(points):
        """Rotate the points using a random rotation matrix."""
        theta = random.uniform(0, 2 * math.pi)  # Random rotation angle in radians
        rotation_matrix = np.array([
            [math.cos(theta), -math.sin(theta)],
            [math.sin(theta), math.cos(theta)]
        ])
        return [np.dot(rotation_matrix, p) for p in points]

    @staticmethod
    def translate_points(points, image_size):
        """Translate the points to a random position within the image."""
        center_x = random.randint(image_size // 4, 3 * image_size // 4)
        center_y = random.randint(image_size // 4, 3 * image_size // 4)
        return [p + [center_x, center_y] for p in points]

    def draw_shape(self, image, points, thickness):
        """Draw a polygon on the image using the given points and thickness."""
        for i in range(len(points)):
            p1 = points[i]
            p2 = points[(i + 1) % len(points)]  # Connect the last point to the first to close the shape
            self.draw_line(image, int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]), thickness=thickness)