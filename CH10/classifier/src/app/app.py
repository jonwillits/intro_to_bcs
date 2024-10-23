import tkinter as tk
import math
from . import interface_frame
from . import drawing_canvas

class App:

    def __init__(self, network, dataset):

        self.network = network
        self.dataset = dataset
        self.root = None

        self.app_dimensions = (1100, 650)

        self.interface_frame = None
        self.current_shape_label = None
        self.shape_instance_entry = None
        self.current_instance_index = None
        self.show_instance_button = None

        self.main_frame = None
        self.drawing_canvas = None
        self.hidden_max_rows = 16
        self.hidden_layer_rows = min(self.network.hidden_size, self.hidden_max_rows)
        self.hidden_cell_size = 20
        self.hidden_cell_spacing = 0
        self.starting_x = 20
        self.starting_y = 20

        self.input_position = (self.starting_x,
                               int(self.hidden_layer_rows*(self.hidden_cell_size+self.hidden_cell_spacing)/2))

        self.hidden_bias_position = (self.input_position[0] + int(self.dataset.image_size/2),
                                     self.input_position[1] - int(self.dataset.image_size) - 20)
        self.hidden_position = (self.input_position[0] + self.dataset.image_size + 50, self.starting_y)


        self.output_position = ()

        self.create_app_window()
        self.create_interface_frame()
        self.create_main_frame()
        self.current_instance_index = tk.IntVar(value=0)

    def create_app_window(self):
        """
        Creates and configures the main window, sets up the button and label layout,
        and initializes the Rock-Paper-Scissors game UI.
        """
        self.root = tk.Tk()
        self.root.title("Shape Classifier")
        self.root.geometry(f"{self.app_dimensions[0]}x{self.app_dimensions[1]}")
        self.root.config(bg="black")
        self.root.update()

    def create_interface_frame(self):
        self.interface_frame = interface_frame.InterfaceFrame(self, self.root)

    def create_main_frame(self):
        # Main frame
        self.main_frame = tk.Frame(self.root, bg="#4574a3", width=self.app_dimensions[0])
        self.main_frame.pack_propagate(False)
        self.main_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.create_drawing_canvas()
        self.draw_network_visualization()

    def create_drawing_canvas(self):
        self.drawing_canvas = drawing_canvas.DrawingCanvas(self.main_frame, self.dataset.image_size)
        self.drawing_canvas.canvas.place(x=self.input_position[0], y=self.input_position[1])
        self.drawing_canvas.draw_matrix(self.dataset.x_list[5])

    def draw_network_visualization(self):
        self.draw_layer(self.main_frame, 1, self.hidden_bias_position, 1, self.hidden_cell_size)
        self.draw_layer(self.main_frame, self.network.hidden_size, self.hidden_position, self.hidden_max_rows, self.hidden_cell_size)

    @staticmethod
    def draw_layer(parent, layer_size, position, max_rows, label_size, unit_spacing=0):

        # Calculate the number of rows (constrained by max_rows) and columns
        num_rows = min(layer_size, max_rows)  # Rows should be at most max_rows
        num_columns = math.ceil(layer_size / num_rows)  # Calculate required columns
        layer_label_list = []
        for i in range(num_columns):
            for j in range(num_rows):
                # Only add labels if the current number of labels is less than the total layer_size
                if len(layer_label_list) < layer_size:
                    square = tk.Label(parent, bg="white",
                                      highlightthickness=1, bd=1, borderwidth=1,
                                      relief="flat", highlightbackground="black")
                    x_pos = position[0] + i * (label_size + unit_spacing)
                    y_pos = position[1] + j * (label_size + unit_spacing)
                    # Place the square at the correct position
                    square.place(x=x_pos,
                                 y=y_pos,
                                 width=label_size, height=label_size)

                    layer_label_list.append(square)

        return layer_label_list

    def update_layer_activation(self, data_matrix):
        current_x = self.dataset.x_list[self.current_instance_index]
        self.network.forward(current_x)
