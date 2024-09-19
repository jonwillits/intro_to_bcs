import tkinter as tk
import math
import numpy as np


class DatasetFrame:

    def __init__(self, app, x, y, height, width):
        self.app = app
        self.current_index = None  # Add current_index to store selected row
        self.frame = tk.Frame(app.main_frame, bg="blue", height=height, width=width)
        self.frame.place(x=x, y=y)
        self.canvas = tk.Canvas(self.frame, bg="#BBBBBB", height=height, width=width, borderwidth=0,
                                highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.thickness = 3

    def on_text_click(self, index):
        """Handler to update current_index when a text item is clicked."""
        self.app.current_item_index = index
        print(f"Row {index} clicked, current_index updated to {self.current_index}")
        self.app.draw_main_frame()

    def draw_frame(self):
        self.canvas.delete("all")

        start_x = 0
        start_y = 0
        button_height = 32
        button_width = 60
        self.canvas.create_text(start_x + 10, start_y + 10, text=f"{self.app.dataset.dataset_name} Dataset:",
                                font="Arial 16 bold", fill="#000000", anchor="nw")

        header = "x1     x2      y         y'        prediction"
        self.canvas.create_text(start_x + 50, start_y + 35, text=header, font="Arial 16 bold", fill="black",
                                anchor="nw")

        self.canvas.create_line(start_x + 39, start_y + 55, start_x + 300, start_y + 55, width=self.thickness,
                                fill="black")
        self.canvas.create_line(start_x + 40, start_y + 55, start_x + 40, start_y + 175, width=self.thickness,
                                fill="black")
        self.canvas.create_line(start_x + 120, start_y + 55, start_x + 120, start_y + 175, width=self.thickness,
                                fill="black")
        self.canvas.create_line(start_x + 160, start_y + 55, start_x + 160, start_y + 175, width=self.thickness,
                                fill="black")
        self.canvas.create_line(start_x + 220, start_y + 55, start_x + 220, start_y + 175, width=self.thickness,
                                fill="black")
        self.canvas.create_line(start_x + 300, start_y + 55, start_x + 300, start_y + 175, width=self.thickness,
                                fill="black")
        self.canvas.create_line(start_x + 38, start_y + 175, start_x + 300, start_y + 175, width=self.thickness,
                                fill="black")

        # Add text items for each row of data and bind click events
        for i in range(self.app.dataset.n):
            x = self.app.dataset.x[i]
            y = self.app.dataset.y[i]
            z, y_predict = self.app.network.forward(x)
            y_predict = y_predict[0, 0]
            guess = np.round(y_predict)
            items = f"{x[0]}       {x[1]}        {y[0]}       {y_predict:0.3f}          {guess:0.0f}"
            tag = "item" + str(i)

            # Create text item and bind it to a click event
            text_id = self.canvas.create_text(start_x + 50, start_y + 35 + (i + 1) * 30,
                                              text=items,
                                              font="Arial 16 bold", fill="black", anchor="nw",
                                              tags=tag)

            # Bind the click event to update current_index when this row is clicked
            self.canvas.tag_bind(text_id, "<Button-1>", lambda event, index=i: self.on_text_click(index))

