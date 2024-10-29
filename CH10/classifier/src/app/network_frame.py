import tkinter as tk
from . import drawing_canvas
from . import layer_frame
from . import utils
import math

class NetworkFrame:

    def __init__(self, app, parent, params):
        self.app = app
        self.parent = parent
        self.bg_color = "#4574a3"

        self.frame_padding = params.App.network_frame_padding

        self.layer_max_rows = params.App.layer_max_rows
        self.layer_spacing = params.App.layer_spacing

        self.unit_size = params.App.unit_size
        self.unit_spacing = params.App.unit_spacing
        self.unit_border = params.App.unit_border
        self.unit_highlight_thickness = params.App.unit_highlight_thickness

        self.hidden_bias_offset = params.App.hidden_bias_offset
        self.hidden_bias_border = params.App.hidden_bias_border
        self.hidden_bias_highlight_thickness = params.App.hidden_bias_highlight_thickness

        self.hidden_frame_padding = params.App.hidden_frame_padding
        self.hidden_frame_border = params.App.hidden_frame_border
        self.hidden_frame_highlight_thickness = params.App.hidden_frame_highlight_thickness

        self.output_frame_padding = params.App.output_frame_padding
        self.output_frame_border = params.App.output_frame_border
        self.output_frame_highlight_thickness = params.App.output_frame_highlight_thickness
        self.output_label_width = params.App.output_label_width

        self.output_bias_offset = params.App.output_bias_offset
        self.output_bias_border = params.App.output_bias_border
        self.output_bias_highlight_thickness = params.App.output_bias_highlight_thickness

        self.params = params

        self.frame = None
        self.frame_dimensions = None

        self.epochs_label = None

        self.input_frame = None
        self.input_frame_dimensions = None
        self.input_layer_shape = (params.Shapes.image_size, params.Shapes.image_size)
        self.input_frame_position = None

        self.hidden_bias_unit = None
        self.hidden_bias_dimensions = None

        self.hidden_layer_frame = None
        self.hidden_frame_dimensions = None
        self.hidden_layer_shape = None
        self.hidden_frame_position = None

        self.output_bias_unit = None
        self.output_bias_dimensions = None

        self.output_layer_frame = None
        self.output_frame_dimensions = None
        self.output_layer_shape = None
        self.output_frame_position = None

        self.output_graph_frame = None
        self.output_graph_dimensions = None
        self.output_graph_position = None

        self.calculate_dimensions()
        self.create_network_frame()
        self.update_network_frame()

    @staticmethod
    def calculate_layer_shape(max_rows, layer_size):
        # Calculate the number of rows (constrained by max_rows) and columns
        num_rows = min(layer_size, max_rows)  # Rows should be at most max_rows
        num_columns = math.ceil(layer_size / num_rows)  # Calculate required columns
        dimensions = (num_rows, num_columns)
        return dimensions

    def calculate_dimensions(self):

        self.hidden_bias_dimensions = (self.unit_size+self.unit_border+self.unit_highlight_thickness,
                                       self.unit_size+self.unit_border+self.unit_highlight_thickness)

        self.output_bias_dimensions = (self.unit_size+self.unit_border+self.unit_highlight_thickness,
                                       self.unit_size+self.unit_border+self.unit_highlight_thickness)

        self.input_frame_dimensions = (self.app.training_set.image_size+2*self.unit_border+2*self.unit_highlight_thickness,
                                       self.app.training_set.image_size+2*self.unit_border+2*self.unit_highlight_thickness)

        self.hidden_layer_shape = self.calculate_layer_shape(self.layer_max_rows, self.app.network.hidden_size)

        self.hidden_frame_dimensions = utils.calculate_layer_frame_dimensions(self.hidden_frame_padding,
                                                                         self.hidden_layer_shape,
                                                                         self.hidden_frame_border,
                                                                         self.hidden_frame_highlight_thickness,
                                                                         self.unit_size,
                                                                         self.unit_spacing,
                                                                         self.unit_border,
                                                                         self.unit_highlight_thickness)

        self.output_layer_shape = (self.app.training_set.num_categories, 1)
        self.output_frame_dimensions = utils.calculate_layer_frame_dimensions(self.output_frame_padding,
                                                                              self.output_layer_shape,
                                                                              self.output_frame_border,
                                                                              self.output_frame_highlight_thickness,
                                                                              self.unit_size,
                                                                              self.unit_spacing,
                                                                              self.unit_border,
                                                                              self.unit_highlight_thickness,
                                                                              label_list=self.app.training_set.category_list,
                                                                              label_width=self.output_label_width)

        input_height = self.input_frame_dimensions[1] + self.hidden_bias_offset + self.hidden_bias_dimensions[1]
        hidden_height = self.hidden_frame_dimensions[1] + self.output_bias_offset + self.hidden_bias_dimensions[1]
        output_height =  self.output_frame_dimensions[1]

        frame_height = max(input_height, hidden_height, output_height) + 2*self.frame_padding
        frame_width = self.input_frame_dimensions[0] + self.hidden_frame_dimensions[0] + self.output_frame_dimensions[0] + 2*self.layer_spacing + 2*self.frame_padding

        self.frame_dimensions = (frame_width, frame_height)

    def create_network_frame(self):

        self.frame = tk.Frame(self.parent, bg=self.bg_color,
                              highlightthickness=1, bd=1, borderwidth=1, relief="solid", highlightbackground="black",
                              height=self.frame_dimensions[1], width=self.frame_dimensions[0])

        self.create_epochs_label()

        self.create_input_layer()

        self.create_hidden_layer()

        self.hidden_bias_unit = self.create_bias_unit(self.frame, self.hidden_bias_dimensions, self.hidden_bias_border,
                                                      self.hidden_bias_highlight_thickness, self.input_frame_position,
                                                      self.input_frame_dimensions, self.hidden_bias_offset)
        self.output_bias_unit = self.create_bias_unit(self.frame, self.output_bias_dimensions, self.output_bias_border,
                                                      self.output_bias_highlight_thickness, self.hidden_frame_position,
                                                      self.hidden_frame_dimensions, self.output_bias_offset)

        self.create_output_layer()
        self.input_hidden_arrow = self.create_arrow_canvas(self.frame, self.hidden_frame_position, self.layer_spacing, self.hidden_frame_dimensions[1])
        self.hidden_output_arrow = self.create_arrow_canvas(self.frame, self.output_frame_position, self.layer_spacing, self.output_frame_dimensions[1])
        self.create_output_graph()

    def create_epochs_label(self):
        self.epochs_label = tk.Label(self.frame, bg=self.bg_color, fg="black",
                         text=f"Epoch: {self.app.network.epoch}", font=("Helvetica", 12),
                         highlightthickness=0, bd=self.unit_border,
                         borderwidth=0)
        self.epochs_label.place(x=5, y=10, anchor="w")

    @staticmethod
    def create_bias_unit(parent, unit_dimensions, border, highlight_thickness, related_frame_position,
                         related_frame_dimensions, offset):
        bias_unit = tk.Label(parent, bg="white",
                             highlightthickness=highlight_thickness, bd=border, borderwidth=border,
                             relief="solid", highlightbackground="black")

        x_pos = related_frame_position[0] + related_frame_dimensions[0]//2 - unit_dimensions[0]//2
        y_pos = related_frame_position[1] - unit_dimensions[1] - offset

        bias_unit.place(x=x_pos, y=y_pos, width=unit_dimensions[0], height=unit_dimensions[1])
        return bias_unit

    def create_input_layer(self):
        self.input_frame = drawing_canvas.DrawingCanvas(self.frame, self.app, self, self.params)
        x_pos = self.frame_padding
        y_pos = (self.frame_dimensions[1] - self.input_frame_dimensions[1]) // 2
        self.input_frame_position = (x_pos, y_pos)
        self.input_frame.canvas.place(x=x_pos, y=y_pos)

    @staticmethod
    def calculate_frame_position(preceding_frame_position, preceding_frame_dimensions,
                                 layer_spacing, frame_dimensions, parent_frame_dimensions):
        x_pos = preceding_frame_position[0] + layer_spacing + preceding_frame_dimensions[0]
        y_pos = (parent_frame_dimensions[1] - frame_dimensions[1]) // 2
        frame_position = (x_pos, y_pos)
        return frame_position

    def create_hidden_layer(self):
        self.hidden_layer_frame = layer_frame.LayerFrame(self.frame,
                                                         self.app.network.hidden_size, self.hidden_layer_shape,
                                                         self.hidden_frame_dimensions,
                                                         frame_padding=self.hidden_frame_padding,
                                                         unit_size=self.unit_size, unit_spacing=self.unit_spacing,
                                                         unit_border=self.unit_border,
                                                         unit_highlight_thickness=self.unit_highlight_thickness,
                                                         layer_border=self.hidden_frame_border,
                                                         layer_highlight_thickness=self.hidden_frame_highlight_thickness)

        self.hidden_frame_position = self.calculate_frame_position(self.input_frame_position, self.input_frame_dimensions,
                                                                   self.layer_spacing,
                                                                   self.hidden_frame_dimensions, self.frame_dimensions)
        self.hidden_layer_frame.frame.place(x=self.hidden_frame_position[0], y=self.hidden_frame_position[1])

    def create_output_layer(self):
        self.output_layer_frame = layer_frame.LayerFrame(self.frame,
                                                         self.app.training_set.num_categories, self.output_layer_shape,
                                                         self.output_frame_dimensions,
                                                         frame_padding=self.output_frame_padding,
                                                         unit_size=self.unit_size, unit_spacing=self.unit_spacing,
                                                         unit_border=self.unit_border,
                                                         unit_highlight_thickness=self.unit_highlight_thickness,
                                                         layer_border=self.hidden_frame_border,
                                                         layer_highlight_thickness=self.hidden_frame_highlight_thickness,
                                                         unit_label_list=self.app.training_set.category_list)

        self.output_frame_position = self.calculate_frame_position(self.hidden_frame_position, self.hidden_frame_dimensions, self.layer_spacing,
                                                                   self.output_frame_dimensions, self.frame_dimensions)
        self.output_layer_frame.frame.place(x=self.output_frame_position[0], y=self.output_frame_position[1])

    def create_arrow_canvas(self, parent, pointed_frame_position, layer_spacing, pointed_frame_height):
        arrow_length = int(layer_spacing * 0.8)
        arrow_padding = (layer_spacing - arrow_length)//2

        # Create a canvas with no extra width or padding
        canvas_width = arrow_length
        canvas_height = 20  # Minimum height for the arrow line thickness
        canvas = tk.Canvas(parent, width=canvas_width, height=canvas_height, bg=self.bg_color, borderwidth=0,
                           highlightthickness=0)

        # Position the canvas to align with the starting frame and center vertically relative to the target frame
        start_x = pointed_frame_position[0] - arrow_length - arrow_padding  # Start from left frame edge
        start_y = pointed_frame_position[1] + (pointed_frame_height // 2) - (canvas_height // 2)  # Center canvas vertically
        canvas.place(x=start_x, y=start_y)

        # Define the start and end points for the arrow line within the canvas
        line_start_x = 0
        line_end_x = arrow_length
        line_y = canvas_height // 2  # Center the arrow line vertically

        # Draw the arrow line from start to end within the canvas
        canvas.create_line(line_start_x, line_y, line_end_x, line_y, arrow=tk.LAST, width=4)

        return canvas

    def create_output_graph(self):
        pass

    def update_network_frame(self, x=None):
        if self.hidden_layer_frame is not None:
            if x is None:
                category_index = self.app.interface_frame.current_instance_index
                x_index = self.app.interface_frame.selected_category_index_list[category_index]
                x = self.app.training_set.x_list[x_index]
            self.input_frame.set_current_input(x)
            self.epochs_label.config(text=f"Epoch: {self.app.network.epoch}")
            h, o = self.app.network.forward(x.flatten())
            h_colors = self.array_to_hex_color_list(h)
            bias_color = self.array_to_hex_color_list([1])
            self.update_units(self.hidden_layer_frame.unit_list, h_colors)
            self.update_units([self.output_bias_unit], bias_color)
            self.update_units([self.hidden_bias_unit], bias_color)
            o_colors = self.array_to_hex_color_list(o)
            self.update_units(self.output_layer_frame.unit_list, o_colors)
            self.frame.update_idletasks()

    @staticmethod
    def update_units(unit_list, color_list):
        for unit, color in zip(unit_list, color_list):
            unit.config(bg=color)

    @staticmethod
    def array_to_hex_color_list(array, min_value=-1, max_value=1):
        color_list = []
        for value in array:

            # Normalize the value to a scale of 0 to 1
            normalized_value = (value - min_value) / (max_value - min_value)

            # Calculate the color based on the normalized value
            if normalized_value <= 0:  # Equivalent to min_value
                color = "#FF0000"  # Red
            elif normalized_value >= 1:  # Equivalent to max_value
                color = "#00FF00"  # Green
            else:
                # Scale between red and white for the lower half
                if normalized_value <= 0.5:
                    ratio = normalized_value * 2
                    red = 255
                    green = int(255 * ratio)
                    blue = int(255 * ratio)
                # Scale between white and green for the upper half
                else:
                    ratio = (normalized_value - 0.5) * 2
                    red = int(255 * (1 - ratio))
                    green = 255
                    blue = int(255 * (1 - ratio))

                color = f"#{red:02X}{green:02X}{blue:02X}"
            color_list.append(color)

        return color_list



