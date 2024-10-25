import tkinter as tk
from . import utils

class LayerFrame:

    def __init__(self, parent, layer_size, layer_dimensions,
                 unit_size=20, unit_spacing=0, unit_border=2, frame_padding=5, layer_border=2):
        self.parent = parent
        self.layer_size = layer_size
        self.layer_dimensions = layer_dimensions
        self.unit_size = unit_size
        self.unit_spacing = unit_spacing
        self.unit_border = unit_border
        self.layer_border = layer_border

        self.frame_padding = frame_padding
        self.frame_dimensions = None
        self.frame = None

        self.create_frame()

    def create_frame(self):
        self.calculate_frame_dimensions()
        self.frame = tk.Frame(self.parent, bg="#777777",
                              highlightthickness=0,
                              bd=self.layer_border, borderwidth=self.layer_border,
                              relief="solid", highlightbackground="black",
                              height=self.frame_dimensions[1], width=self.frame_dimensions[0])
        self.draw_layer()

    def calculate_frame_dimensions(self):
        width = self.layer_dimensions[1]*(self.unit_size+self.unit_spacing + 2*self.unit_border) + 2*self.frame_padding
        height = self.layer_dimensions[0] * (self.unit_size + self.unit_spacing + 2*self.unit_border) + 2 * self.frame_padding
        self.frame_dimensions = (width, height)

    def draw_layer(self):

        layer_label_list = []
        for i in range(self.layer_dimensions[1]):
            for j in range(self.layer_dimensions[0]):
                # Only add labels if the current number of labels is less than the total layer_size
                if len(layer_label_list) < self.layer_size:
                    square = tk.Label(self.frame, bg="white",
                                      highlightthickness=0, bd=self.unit_border, borderwidth=self.unit_border,
                                      relief="solid", highlightbackground="black")
                    x_pos = self.frame_padding + i * (self.unit_size + self.unit_spacing + self.unit_border)
                    y_pos = self.frame_padding + j * (self.unit_size + self.unit_spacing + self.unit_border)
                    # Place the square at the correct position
                    square.place(x=x_pos,
                                 y=y_pos,
                                 width=self.unit_size, height=self.unit_size)

                    layer_label_list.append(square)

        return layer_label_list

