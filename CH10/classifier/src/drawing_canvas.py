import tkinter as tk
import numpy as np
import os
import tempfile
from PIL import Image, ImageOps, ImageChops, ImageGrab

class DrawingCanvas:
    def __init__(self, parent, image_size):

        self.parent = parent
        # Create a canvas widget
        self.image_size = image_size
        self.canvas = tk.Canvas(parent, bg="white", width=image_size, height=image_size, highlightthickness=0, bd=0)

        # Initialize variables to track the position and eraser mode
        self.last_x = None
        self.last_y = None
        self.eraser_mode = False
        self.bg_color = "white"  # Background color for eraser

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.on_button_press)  # Left-click to start drawing
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)  # Mouse drag to draw
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)  # Release to stop drawing

        self.canvas.bind("<Button-2>", self.on_button_press_eraser)  # Middle button for eraser
        self.canvas.bind("<B2-Motion>", self.on_mouse_drag)  # Mouse drag for erasing
        self.canvas.bind("<ButtonRelease-2>", self.on_button_release)  # Release to stop erasing

        # Detect CTRL key with Button-1 for eraser
        self.canvas.bind("<Control-B1-Motion>", self.on_mouse_drag_eraser)  # CTRL + Left mouse drag

    def on_button_press(self, event):
        """Handle mouse button press event (start drawing)."""
        self.last_x, self.last_y = event.x, event.y  # Track the initial click position
        self.eraser_mode = False  # Not in eraser mode for normal drawing

    def on_button_press_eraser(self, event):
        """Handle mouse button press event (start erasing with Button-2)."""
        self.last_x, self.last_y = event.x, event.y  # Track the initial click position
        self.eraser_mode = True  # Enter eraser mode

    def on_mouse_drag(self, event):
        """Handle mouse drag event (draw or erase while dragging)."""
        if self.last_x is not None and self.last_y is not None:
            # Determine the color based on whether we're in eraser mode or drawing mode
            color = self.bg_color if self.eraser_mode else "black"
            # Draw a line from the last position to the current mouse position
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=color, width=5)
            # Update the last position to the current position
            self.last_x, self.last_y = event.x, event.y

        # Record the canvas after every mouse drag
        self.record_canvas()

    def on_mouse_drag_eraser(self, event):
        """Handle mouse drag event when CTRL is held (erase with CTRL + Button-1)."""
        if self.last_x is not None and self.last_y is not None:
            # Eraser mode: set color to the background color
            color = self.bg_color
            # Draw a line that "erases"
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=color, width=5)
            # Update the last position to the current position
            self.last_x, self.last_y = event.x, event.y

        # Record the canvas after every mouse drag
        self.record_canvas()

    def on_button_release(self, event):
        """Handle mouse button release event (stop drawing or erasing)."""
        self.last_x, self.last_y = None, None  # Reset the tracking when the mouse button is released

    def record_canvas(self):
        """Capture the canvas to a NumPy matrix with 1s and 0s."""
        # Get the coordinates of the canvas on the screen
        x = self.parent.winfo_rootx() + self.canvas.winfo_x()
        y = self.parent.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()

        # Capture the canvas as an image using ImageGrab
        img = ImageGrab.grab((x, y, x1, y1))

        # Convert the image to grayscale and then to black-and-white (1 for drawn areas, 0 for background)
        bw_img = img.convert('L').point(lambda x: 0 if x > 150 else 1, mode='1')

        # Convert the PIL image to a NumPy array (which will initially be True/False)
        canvas_array = np.array(bw_img)

        # Convert boolean array (True/False) to 1/0
        canvas_array = canvas_array.astype(np.uint8)
        np.set_printoptions(threshold=np.inf, linewidth=np.inf)
        print(canvas_array)  # You can print the array to verify its content, or store it as needed.

        return canvas_array  # Return the NumPy array for further use.

    def draw_matrix(self, flattened_array):

        matrix = np.reshape(flattened_array, (self.image_size, self.image_size))
        """Draw a NumPy matrix to the canvas."""
        rows, cols = matrix.shape
        for row in range(rows):
            for col in range(cols):
                if matrix[row, col] == 1:  # Draw for value 1 (you can modify this for different values)
                    # Draw a pixel as a small rectangle or point
                    self.canvas.create_rectangle(col, row, col + 1, row + 1, outline="", fill="black")
