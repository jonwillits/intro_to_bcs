import tkinter as tk
from . import drawing_canvas
from . import layer_frame
import math

class NetworkFrame:

    def __init__(self, app, parent):
        self.app = app
        self.parent = parent


        self.unit_size = 20
        self.unit_spacing = 0
        self.unit_border = 2
        self.layer_spacing = 50
        self.max_layer_rows = 16


        self.frame = None
        self.frame_dimensions = None
        self.frame_padding = 20

        self.drawing_canvas = None
        self.input_layer_dimensions = None
        self.input_layer_position = None
        self.input_layer_border = 2

        self.hidden_bias_unit = None
        self.hidden_bias_dimensions = None

        self.hidden_layer_frame = None
        self.hidden_layer_dimensions = None
        self.hidden_layer_shape = None
        self.hidden_layer_position = None
        self.hidden_layer_padding = 5
        self.hidden_layer_border = 2

        self.output_bias_unit = None
        self.output_bias_dimensions = None

        self.output_layer_frame = None
        self.output_layer_dimensions = None
        self.output_layer_position = None

        self.output_graph_frame = None
        self.output_graph_dimensions = None
        self.output_graph_position = None

        self.calculate_dimensions()
        self.create_network_frame()

    @staticmethod
    def calculate_layer_shape(max_rows, layer_size):
        # Calculate the number of rows (constrained by max_rows) and columns
        num_rows = min(layer_size, max_rows)  # Rows should be at most max_rows
        num_columns = math.ceil(layer_size / num_rows)  # Calculate required columns
        dimensions = (num_rows, num_columns)
        return dimensions

    def calculate_dimensions(self):

        self.input_layer_dimensions = (self.app.dataset.image_size+2*self.unit_border,
                                       self.app.dataset.image_size+2*self.unit_border)

        self.hidden_bias_dimensions = (self.unit_size, self.unit_size)
        self.hidden_layer_shape = self.calculate_layer_shape(self.max_layer_rows, self.app.network.hidden_size)
        self.hidden_layer_dimensions = (self.hidden_layer_shape[1]*self.unit_size + self.unit_spacing*(self.hidden_layer_shape[1]-1) + 2*self.unit_border,
                                        self.hidden_layer_shape[0]*self.unit_size + self.unit_spacing*(self.hidden_layer_shape[0]-1) + 2*self.unit_border)
        self.output_bias_dimensions = (self.unit_size, self.unit_size)
        self.output_layer_dimensions = (self.unit_size, self.app.dataset.num_categories*(self.unit_size+self.unit_spacing))

        print(self.input_layer_dimensions)
        print(self.hidden_layer_dimensions)
        print(self.output_layer_dimensions)

        frame_height = max(self.input_layer_dimensions[1],  self.hidden_layer_dimensions[1], self.output_layer_dimensions[1])
        frame_width = self.input_layer_dimensions[1] + self.hidden_layer_dimensions[1] + self.output_layer_dimensions[1] + 2*self.layer_spacing + 2*self.frame_padding

        self.frame_dimensions = (frame_width, frame_height)


    def create_network_frame(self):

        self.frame = tk.Frame(self.parent, bg="#4574a3",
                              highlightthickness=1, bd=1, borderwidth=1, relief="solid", highlightbackground="black",
                              height=self.frame_dimensions[1], width=self.frame_dimensions[0])
        self.create_input_layer()
        self.create_bias_units()

        self.create_hidden_layer()

        self.create_output_layer()
        self.create_output_graph()

    def create_bias_units(self):
        self.hidden_bias_unit = tk.Label(self.frame, bg="white",
                                      highlightthickness=0, bd=2, borderwidth=2,
                                      relief="solid", highlightbackground="black")
        x_pos = self.frame_padding + self.input_layer_dimensions[0]//2
        y_pos = ((self.frame_dimensions[1] - self.input_layer_dimensions[1]) // 2) - self.unit_size - 10
        self.hidden_bias_unit.place(x=x_pos, y=y_pos, width=self.unit_size, height=self.unit_size)

        # self.output_bias_unit = tk.Label(self.frame, bg="white",
        #                               highlightthickness=1, bd=1, borderwidth=1,
        #                               relief="flat", highlightbackground="black")
        # self.output_bias_unit.place(x=0, y=0)

    def create_input_layer(self):
        self.drawing_canvas = drawing_canvas.DrawingCanvas(self.frame, self.app.dataset.image_size,
                                                           self.input_layer_border)
        x_pos = self.frame_padding
        y_pos = (self.frame_dimensions[1] - self.input_layer_dimensions[1]) // 2
        self.input_layer_position = (x_pos, y_pos)
        self.drawing_canvas.canvas.place(x=x_pos, y=y_pos)
        self.drawing_canvas.draw_matrix(self.app.dataset.x_list[self.app.current_instance_index])

    def create_hidden_layer(self):
        self.hidden_layer_frame = layer_frame.LayerFrame(self.frame, self.app.network.hidden_size,
                                                         self.hidden_layer_shape, self.unit_size, self.unit_spacing,
                                                         frame_padding=self.hidden_layer_padding,
                                                         layer_border=self.hidden_layer_border)
        x_pos = self.input_layer_position[0] + self.layer_spacing + self.input_layer_dimensions[0]
        y_pos = (self.frame_dimensions[1] - self.hidden_layer_dimensions[1]) // 2
        self.hidden_layer_position = (x_pos, y_pos)
        self.hidden_layer_frame.frame.place(x=x_pos, y=y_pos)

    def create_output_layer(self):
        pass

    def create_output_graph(self):
        pass

    def update_activations(self):
        pass