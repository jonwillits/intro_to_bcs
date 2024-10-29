import tkinter as tk
import numpy as np

class DrawingCanvas:
    def __init__(self, parent, app, network_frame, params):
        self.parent = parent
        self.network_frame = network_frame
        self.app = app
        self.params = params
        self.bg_color = "white"

        # Set thickness for the brush (1 = 1-pixel radius, 2 = 3x3 area, etc.)
        self.thickness = 2  # Adjust thickness as needed

        # Create the canvas widget
        self.canvas = tk.Canvas(parent, bg=self.bg_color, width=self.params.Shapes.image_size,
                                height=self.params.Shapes.image_size,
                                highlightthickness=self.params.App.input_layer_highlight_thickness,
                                bd=self.params.App.input_layer_border, borderwidth=self.params.App.input_layer_border,
                                relief="solid", highlightbackground="black")
        self.canvas.pack()

        # Reference to the current input array, reshaped to match the canvas
        self.set_current_input(self.app.training_set.x_list[self.app.interface_frame.selected_category_index_list[0]])

        # Bind mouse events to handle drawing
        self.canvas.bind("<Button-1>", self.on_draw)
        self.canvas.bind("<B1-Motion>", self.on_draw)

    def set_current_input(self, current_input_array):
        """Set the current input and draw it on the canvas."""
        self.current_input = current_input_array.reshape((self.params.Shapes.image_size, self.params.Shapes.image_size))

    def draw_matrix(self):
        """Draw a NumPy matrix to the canvas."""
        self.canvas.delete("all")

        # Offset to account for highlight thickness
        offset = self.params.App.input_layer_highlight_thickness
        rows, cols = self.current_input.shape

        for row in range(rows):
            for col in range(cols):
                if self.current_input[row, col] == 1:
                    self.canvas.create_rectangle(
                        col + offset, row + offset, col + 1 + offset, row + 1 + offset, fill="black", outline=""
                    )
        self.canvas.update_idletasks()

    def on_draw(self, event):
        """Handle drawing on the canvas with the left mouse button, with adjustable thickness."""
        # Calculate the offset due to border and highlight thickness
        border_width = int(self.canvas.cget('borderwidth'))
        highlight_thickness = int(self.canvas.cget('highlightthickness'))
        offset = border_width + highlight_thickness

        # Get the canvas coordinates of the click, adjusted for the offset
        x = event.x - offset
        y = event.y - offset

        # Ensure the coordinates are within bounds
        if 0 <= x < self.params.Shapes.image_size and 0 <= y < self.params.Shapes.image_size:
            # Convert the canvas coordinates to array indices
            center_row = int(y)
            center_col = int(x)

            # Update all pixels within the specified thickness radius
            for dy in range(-self.thickness, self.thickness + 1):
                for dx in range(-self.thickness, self.thickness + 1):
                    # Check if within the circular brush radius
                    if dx**2 + dy**2 <= self.thickness**2:
                        row = center_row + dy
                        col = center_col + dx
                        # Make sure we stay within bounds
                        if 0 <= row < self.params.Shapes.image_size and 0 <= col < self.params.Shapes.image_size:
                            # Set the pixel to black in the input array
                            self.current_input[row, col] = 1

            # Redraw the matrix to reflect the changes
            self.network_frame.update_network_frame()
