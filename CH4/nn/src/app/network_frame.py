import tkinter as tk
import math
import numpy as np

class NetworkFrame:

    def __init__(self, app, x, y, height, width):
        self.app = app
        self.frame = tk.Frame(app.main_frame, bg="blue", height=height, width=width)
        self.frame.place(x=x, y=y)
        self.canvas = tk.Canvas(self.frame, bg="#BBBBBB", height=height, width=width, borderwidth=0, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.node_radius = 30
        self.thickness = 3
        self.y0_pos = (500, 175)
        self.x0_pos = (150, 75)
        self.x1_pos = (150, 175)
        self.x2_pos = (150, 275)

    def draw_frame(self):
        self.canvas.delete("all")
        self.draw_weights()
        self.draw_nodes()


    def draw_nodes(self):
        x = self.app.dataset.x[self.app.current_item_index]
        z, y = self.app.network.forward(x)
        start_x = 0
        start_y = 0
        button_height = 32
        button_width = 60
        self.canvas.create_text(start_x+10, start_y+10, text="Network Diagram:",
                                font="Arial 16 bold", fill="#000000", anchor="nw")

        y0 = self.canvas.create_oval(self.y0_pos[0]-self.node_radius,
                                     self.y0_pos[1]-self.node_radius,
                                     self.y0_pos[0]+self.node_radius,
                                     self.y0_pos[1]+self.node_radius,
                                     width=self.thickness, fill=self.get_hex_color(y[0][0]), outline="#000000")
        self.canvas.create_text(self.y0_pos[0],
                                self.y0_pos[1]-self.node_radius*1.5,
                                text="y".format(y[0][0]), font="Arial 16 bold", fill="black")
        self.canvas.create_text(self.y0_pos[0],
                                self.y0_pos[1],
                                text="{:0.3f}".format(y[0][0]), font="Arial 16 bold", fill="black")

        x0 = self.canvas.create_oval(self.x0_pos[0] - self.node_radius,
                                     self.x0_pos[1] - self.node_radius,
                                     self.x0_pos[0] + self.node_radius,
                                     self.x0_pos[1] + self.node_radius,
                                     width=self.thickness, fill=self.get_hex_color(1), outline="#000000")
        self.canvas.create_text(self.x0_pos[0],
                                self.x0_pos[1]+self.node_radius*1.5,
                                text="x0 (bias)", font="Arial 16 bold", fill="black")
        self.canvas.create_text(self.x0_pos[0],
                                self.x0_pos[1],
                                text="1", font="Arial 16 bold", fill="black")

        x1 = self.canvas.create_oval(self.x1_pos[0] - self.node_radius,
                                     self.x1_pos[1] - self.node_radius,
                                     self.x1_pos[0] + self.node_radius,
                                     self.x1_pos[1] + self.node_radius,
                                     width=self.thickness, fill=self.get_hex_color(x[0]), outline="#000000")
        self.canvas.create_text(self.x1_pos[0],
                                self.x1_pos[1]+self.node_radius*1.5,
                                text="x1", font="Arial 16 bold", fill="black")
        self.canvas.create_text(self.x1_pos[0],
                                self.x1_pos[1],
                                text=x[0], font="Arial 16 bold", fill="black")

        x2 = self.canvas.create_oval(self.x2_pos[0] - self.node_radius,
                                     self.x2_pos[1] - self.node_radius,
                                     self.x2_pos[0] + self.node_radius,
                                     self.x2_pos[1] + self.node_radius,
                                     width=self.thickness, fill=self.get_hex_color(x[1]), outline="#000000")
        self.canvas.create_text(self.x2_pos[0],
                                self.x2_pos[1]+self.node_radius*1.5,
                                text="x2", font="Arial 16 bold", fill="black")
        self.canvas.create_text(self.x2_pos[0],
                                self.x2_pos[1],
                                text=x[1], font="Arial 16 bold", fill="black")

    def draw_weights(self):
        # For right center of x0 (x0_pos)
        b0_x1 = self.x0_pos[0] + self.node_radius  # Right edge of x0
        b0_y1 = self.x0_pos[1]  # Vertical center of x0

        # For left center of y0 (y0_pos)
        b0_x2 = self.y0_pos[0] - self.node_radius  # Left edge of y0
        b0_y2 = self.y0_pos[1]  # Vertical center of y0

        # Draw the line
        b0_value = self.app.network.y_bias[0][0]
        b0 = self.canvas.create_line(b0_x1, b0_y1, b0_x2, b0_y2,
                                     width=self.thickness,
                                     fill=self.get_hex_color(b0_value))

        # Similarly for x1 and x2:
        # Right center of x1 (x1_pos)
        b1_x1 = self.x1_pos[0] + self.node_radius  # Right edge of x1
        b1_y1 = self.x1_pos[1]  # Vertical center of x1

        # Draw line from x1 to y0
        b1_value = self.app.network.y_x[0, 0]
        b1 = self.canvas.create_line(b1_x1, b1_y1, b0_x2, b0_y2,  # Use same b0_x2 and b0_y2 for left center of y0
                                     width=self.thickness,
                                     fill=self.get_hex_color(b1_value))

        # Right center of x2 (x2_pos)

        b2_x1 = self.x2_pos[0] + self.node_radius  # Right edge of x2
        b2_y1 = self.x2_pos[1]  # Vertical center of x2

        # Draw line from x2 to y0
        b2_value = self.app.network.y_x[0, 1]
        b2 = self.canvas.create_line(b2_x1, b2_y1, b0_x2, b0_y2,  # Use same b0_x2 and b0_y2 for left center of y0
                                     width=self.thickness,
                                     fill=self.get_hex_color(b2_value))

        self.canvas.create_text(self.y0_pos[0]-150, self.y0_pos[1]-80,
                                        text=f"b0 = {b0_value:0.3f}",
                                        font="Arial 16 bold", fill="black", tags='b0')

        self.canvas.create_text(self.y0_pos[0]-150, self.y0_pos[1],
                                        text=f"b1 = {b1_value:0.3f}",
                                        font="Arial 16 bold", fill="black", tags='b1')

        self.canvas.create_text(self.y0_pos[0]-150, self.y0_pos[1]+80,
                                        text=f"b2 = {b2_value:0.3f}",
                                        font="Arial 16 bold", fill="black", tags='b2')


    def get_hex_color(self, value):
        if value > 1:
            value = 1
        if value < -1:
            value = -1

        abs_value = 1 - abs(value)
        scaled_value = int(round(255 * abs_value, 0))
        hex_value = hex(scaled_value)[2:]

        if len(hex_value) == 1:
            hex_value = "0" + hex_value

        if value > 0:
            return '#{}ff{}'.format(hex_value, hex_value)
        elif value < 0:
            return '#ff{}{}'.format(hex_value, hex_value)
        else:
            return "#ffffff"