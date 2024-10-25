import tkinter as tk

class InterfaceFrame:

    def __init__(self, app, parent):

        self.app = app
        self.parent = parent

        self.height = 30
        self.width = parent.winfo_width()

        self.frame = None
        self.current_shape_label = None
        self.shape_instance_entry = None
        self.show_instance_button = None

        self.create_frame()
        self.add_widgets()

    def create_frame(self):
        self.frame = tk.Frame(self.parent, bg="#222222",
                 height=self.height, width=self.width)
        self.frame.pack_propagate(False)

        self.current_shape_label = tk.Label(self.frame, text="Current Shape Instance", fg="white",
                                            bg="#222222")
        self.current_shape_label.pack(side=tk.LEFT, padx=10, pady=5)

    def add_widgets(self):
        # Add the entry widget

        self.shape_instance_entry = tk.Entry(self.frame, textvariable=self.app.current_instance_index, width=10)
        self.shape_instance_entry.pack(side=tk.LEFT, padx=10, pady=5)
        self.shape_instance_entry.insert(0, self.app.current_instance_index)

        self.show_instance_button = tk.Button(self.frame, text="Show!", command=self.show_instance)
        self.show_instance_button.pack(side=tk.LEFT, padx=10, pady=5)

    def show_instance(self):
        # Get the value from the entry widget
        try:
            self.app.displayed_current_instance_index.set(int(self.shape_instance_entry.get()))
            self.app.current_instance_index = self.app.displayed_current_instance_index.get()
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return

        # Check if the index is in the valid range
        if 0 <= self.app.current_instance_index < self.app.dataset.dataset_size:
            try:
                # Draw the matrix corresponding to the current index
                self.app.network_frame.drawing_canvas.draw_matrix(self.app.dataset.x_list[self.app.current_instance_index])
            except IndexError:
                print(f"Index {self.parent.current_instance_index} is out of range.")
        else:
            print(f"Index {self.parent.current_instance_index} is out of range. Valid range: 0 to {self.app.dataset.dataset_size - 1}")
