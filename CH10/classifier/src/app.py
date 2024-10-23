import tkinter as tk
from . import drawing_canvas

class App:

    def __init__(self, the_network, the_dataset):

        self.the_network = the_network
        self.the_dataset = the_dataset
        self.root = None

        self.app_dimensions = (1100, 650)
        self.interface_frame_height = 30
        self.main_frame_height = self.app_dimensions[0] - self.interface_frame_height

        self.interface_frame = None
        self.main_frame = None
        self.drawing_canvas = None

        self.current_shape_label = None
        self.shape_instance_entry = None
        self.current_instance = None
        self.show_instance_button = None

        self.create_app_window()
        self.create_interface_frame()
        self.create_main_frame()

    def create_app_window(self):
        """
        Creates and configures the main window, sets up the button and label layout,
        and initializes the Rock-Paper-Scissors game UI.
        """
        self.root = tk.Tk()
        self.root.title("Shape Classifier")
        self.root.geometry(f"{self.app_dimensions[0]}x{self.app_dimensions[1]}")
        self.root.config(bg="black")

    def create_interface_frame(self):
        self.interface_frame = tk.Frame(self.root, bg="#222222",
                                        height=self.interface_frame_height, width=self.app_dimensions[0])
        self.interface_frame.pack_propagate(False)
        self.interface_frame.pack(side=tk.TOP, fill=tk.X)

        self.current_shape_label = tk.Label(self.interface_frame, text="Current Shape Instance", fg="white",
                                            bg="#222222")
        self.current_shape_label.pack(side=tk.LEFT, padx=10, pady=5)

        # Add the entry widget
        self.current_instance = tk.IntVar(value=0)
        self.shape_instance_entry = tk.Entry(self.interface_frame, textvariable=self.current_instance, width=10)
        self.shape_instance_entry.pack(side=tk.LEFT, padx=10, pady=5)

        self.show_instance_button = tk.Button(self.interface_frame, text="Show!", command=self.show_instance)
        self.show_instance_button.pack(side=tk.LEFT, padx=10, pady=5)

    def create_main_frame(self):

        # Main frame
        self.main_frame = tk.Frame(self.root, bg="green", height=self.main_frame_height, width=self.app_dimensions[0])
        self.main_frame.pack_propagate(False)
        self.main_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.create_drawing_canvas()

    def create_drawing_canvas(self):
        self.drawing_canvas = drawing_canvas.DrawingCanvas(self.main_frame, self.the_dataset.image_size)
        self.drawing_canvas.canvas.place(x=20, y=20)
        self.drawing_canvas.draw_matrix(self.the_dataset.x_list[5])

    def show_instance(self):
        # Get the value from the entry widget
        try:
            current_x_index = int(self.shape_instance_entry.get())
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return

        # Check if the index is in the valid range
        if 0 <= current_x_index < self.the_dataset.dataset_size:
            try:
                # Clear the canvas
                self.drawing_canvas.canvas.delete("all")

                # Draw the matrix corresponding to the current index
                self.drawing_canvas.draw_matrix(self.the_dataset.x_list[current_x_index])
            except IndexError:
                print(f"Index {current_x_index} is out of range.")
        else:
            print(f"Index {current_x_index} is out of range. Valid range: 0 to {self.the_dataset.dataset_size - 1}")

