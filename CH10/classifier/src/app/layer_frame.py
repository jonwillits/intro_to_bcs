import tkinter as tk

class LayerFrame:

    def __init__(self, parent, layer_size, layer_shape, frame_dimensions, frame_padding=5,
                 unit_size=20, unit_spacing=0, unit_border=2, unit_highlight_thickness=2,
                 layer_border=2, layer_highlight_thickness=2, unit_label_list=None):
        self.parent = parent
        self.layer_size = layer_size
        self.layer_shape = layer_shape
        self.unit_size = unit_size
        self.unit_spacing = unit_spacing
        self.unit_border = unit_border
        self.unit_highlight_thickness = unit_highlight_thickness
        self.layer_border = layer_border
        self.layer_highlight_thickness = layer_highlight_thickness
        self.unit_label_list = unit_label_list
        self.unit_label_offset = 10
        self.frame_bg_color = "#CCCCCC"
        self.unit_list = None

        self.frame_padding = frame_padding
        self.frame_dimensions = frame_dimensions
        self.frame = None

        self.create_frame()

    def create_frame(self):
        self.frame = tk.Frame(self.parent, bg=self.frame_bg_color,
                              highlightthickness=self.layer_highlight_thickness,
                              bd=self.layer_border, borderwidth=self.layer_border,
                              relief="solid", highlightbackground="black",
                              height=self.frame_dimensions[1], width=self.frame_dimensions[0])
        self.unit_list = self.draw_layer()

    def draw_layer(self):
        layer_label_list = []
        final_x = 0
        for i in range(self.layer_shape[1]):
            for j in range(self.layer_shape[0]):
                # Only add labels if the current number of labels is less than the total layer_size
                if len(layer_label_list) < self.layer_size:
                    square = tk.Label(self.frame, bg="white",
                                      highlightthickness=self.unit_highlight_thickness, bd=self.unit_border,
                                      borderwidth=self.unit_border,
                                      relief="solid", highlightbackground="black")
                    x_pos = self.frame_padding + i * (self.unit_size + self.unit_spacing + self.unit_border + self.unit_highlight_thickness)
                    y_pos = self.frame_padding + j * (self.unit_size + self.unit_spacing + self.unit_border + self.unit_highlight_thickness)
                    # Place the square at the correct position
                    square.place(x=x_pos,
                                 y=y_pos,
                                 width=self.unit_size, height=self.unit_size)
                    layer_label_list.append(square)
                    final_x = x_pos

        if self.unit_label_list is not None:
            x_pos = final_x + + self.unit_label_offset + self.unit_size//2
            for i in range(self.layer_shape[0]):
                y_pos = self.frame_padding + i * (self.unit_size + self.unit_spacing + self.unit_border + self.unit_highlight_thickness) + self.unit_size//2 + self.unit_border + self.unit_highlight_thickness
                label = tk.Label(self.frame, bg=self.frame_bg_color, fg="black",
                                  text=self.unit_label_list[i], font=("Helvetica", 12),
                                  highlightthickness=0, bd=self.unit_border,
                                  borderwidth=0)
                label.place(x=x_pos, y=y_pos, height=self.unit_size, anchor="w")

        return layer_label_list

