import tkinter as tk

class NetworkFrame:

    def __init__(self, parent, position, num_units, max_columns, unit_size, unit_spacing):
        self.parent = parent
        self.position = position
        self.num_units = num_units
        self.max_columns = max_columns
        self.unit_size = unit_size
        self.unit_spacing = unit_spacing
        self.frame_padding = 10

        self.frame = tk.Frame(self.parent, bg="#222222")
        self.frame.pack_propagate(False)
        self.frame.pack(side=tk.TOP, fill=tk.X)

    def adjust_frame_size(self, frame):
        # Get the bounding box (min/max coordinates of all children)
        max_x, max_y = 0, 0
        for widget in self.frame.winfo_children():
            # Get widget's coordinates and size
            widget.update_idletasks()  # Ensure that geometry info is updated
            x = widget.winfo_x()
            y = widget.winfo_y()
            width = widget.winfo_width()
            height = widget.winfo_height()

            # Determine the bottom-right corner of the widget
            max_x = max(max_x, x + width)
            max_y = max(max_y, y + height)

        # Set the frame size to fit all children
        frame.config(width=max_x+self.frame_padding, height=max_y+self.frame_padding)