import tkinter as tk
import math
import numpy as np

class NetworkFrame:

    def __init__(self, app):
        self.app = app
        self.frame = tk.Frame(app.main_frame, bg="blue", height=200, width=300)
        self.frame.place(x=0, y=0)
        self.canvas = tk.Canvas(self.frame, bg="#BBBBBB", height=200, width=300, borderwidth=0, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.node_radius = 30
        self.y0_pos = (350, 200)
        self.x0_pos = (100, 350)
        self.x1_pos = (250, 500)
        self.x2_pos = (450, 500)

    def draw_frame(self):
        self.canvas.delete("all")
        self.draw_nodes()
        self.draw_weights()

    def draw_nodes(self):
        x = self.app.dataset.x[self.app.current_item_index]
        z, y = self.app.network.forward(x)
    #     self.y0 = self.network_canvas.create_oval(self.y0_pos[0]-self.node_radius, self.y0_pos[1]-self.node_radius,
    #                                               self.y0_pos[0]+self.node_radius, self.y0_pos[1]+self.node_radius,
    #                                               width=self.thickness, fill=self.get_hex_color(y[0][0]))
    #     self.network_canvas.create_text(self.y0_pos[0], self.y0_pos[1]-self.node_radius*1.5,
    #                                     text="y".format(y[0][0]), font="Arial 16 bold")
    #     self.network_canvas.create_text(self.y0_pos[0], self.y0_pos[1],
    #                                     text="{:0.3f}".format(y[0][0]), font="Arial 16 bold")
    #
    #     self.x0 = self.network_canvas.create_oval(self.x0_pos[0] - self.node_radius, self.x0_pos[1] - self.node_radius,
    #                                               self.x0_pos[0] + self.node_radius, self.x0_pos[1] + self.node_radius,
    #                                               width=self.thickness, fill=self.get_hex_color(1))
    #     self.network_canvas.create_text(self.x0_pos[0], self.x0_pos[1]+self.node_radius*1.5,
    #                                     text="x0 (bias)", font="Arial 16 bold")
    #     self.network_canvas.create_text(self.x0_pos[0], self.x0_pos[1],
    #                                     text="1", font="Arial 16 bold")
    #
    #
    #     self.x1 = self.network_canvas.create_oval(self.x1_pos[0] - self.node_radius, self.x1_pos[1] - self.node_radius,
    #                                               self.x1_pos[0] + self.node_radius, self.x1_pos[1] + self.node_radius,
    #                                               width=self.thickness, fill=self.get_hex_color(x[0]))
    #     self.network_canvas.create_text(self.x1_pos[0], self.x1_pos[1]+self.node_radius*1.5,
    #                                     text="x1", font="Arial 16 bold")
    #     self.network_canvas.create_text(self.x1_pos[0], self.x1_pos[1],
    #                                     text="{:0.0f}".format(x[0]), font="Arial 16 bold")
    #
    #     self.x2 = self.network_canvas.create_oval(self.x2_pos[0] - self.node_radius, self.x2_pos[1] - self.node_radius,
    #                                               self.x2_pos[0] + self.node_radius, self.x2_pos[1] + self.node_radius,
    #                                               width=self.thickness, fill=self.get_hex_color(x[1]))
    #     self.network_canvas.create_text(self.x2_pos[0], self.x2_pos[1]+self.node_radius*1.5,
    #                                     text="x2", font="Arial 16 bold")
    #     self.network_canvas.create_text(self.x2_pos[0], self.x2_pos[1],
    #                                     text="{:0.0f}".format(x[1]), font="Arial 16 bold")
    #
    def draw_weights(self):
        b0_x1 = self.x0_pos[0]+(self.node_radius/(2**0.5))
        b0_x2 = self.y0_pos[0]
        b0_y1 = self.x0_pos[1]-(self.node_radius/(2**0.5))
        b0_y2 = self.y0_pos[1]+self.node_radius
        self.b0 = self.network_canvas.create_line(b0_x1, b0_y1, b0_x2, b0_y2,
                                                  width=self.thickness,
                                                  fill=self.get_hex_color(self.network.y_bias[0][0]))
    #
    #     self.network_canvas.create_text(self.y0_pos[0]-160, self.y0_pos[1]+80,
    #                                     text="b0 = {:0.3f}".format(self.network.y_bias[0][0]),
    #                                     font="Arial 16 bold", fill="black", tags='b0')
    #
    #     self.b1 = self.network_canvas.create_line(self.x1_pos[0], self.x1_pos[1]-self.node_radius,
    #                                               self.y0_pos[0], self.y0_pos[1]+self.node_radius,
    #                                               width=self.thickness, fill=self.get_hex_color(self.network.y_x[0][0]))
    #     self.network_canvas.create_text(self.y0_pos[0]-80, self.y0_pos[1]+150,
    #                                     text="b1 = {:0.3f}".format(self.network.y_x[0][0]),
    #                                     font="Arial 16 bold", fill="black", tags='b1')
    #
    #
    #     self.b2 = self.network_canvas.create_line(self.x2_pos[0], self.x2_pos[1]-self.node_radius,
    #                                               self.y0_pos[0], self.y0_pos[1]+self.node_radius,
    #                                               width=self.thickness, fill=self.get_hex_color(self.network.y_x[0][1]))
    #     self.network_canvas.create_text(self.y0_pos[0]+80, self.y0_pos[1]+150,
    #                                     text="b2 = {:0.3f}".format(self.network.y_x[0][1]),
    #                                     font="Arial 16 bold", fill="black", tags='b2')