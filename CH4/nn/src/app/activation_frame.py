import tkinter as tk
import math
import numpy as np

class ActivationFrame:

    def __init__(self, app):
        self.app = app
        self.frame = tk.Frame(app.main_frame, bg="blue", height=200, width=300)
        self.frame.place(x=0, y=0)
        self.canvas = tk.Canvas(self.frame, bg="#BBBBBB", height=200, width=300, borderwidth=0, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def draw_frame(self):
        self.canvas.delete("all")
        thickness = 3

        x_is_min = 40
        y_is_0 = 140
        x_scale = 200
        y_scale = 100

        intervals = np.linspace(-5, 5, 100)
        curve_list = []
        for z in intervals:
            y = 1 / (1 + math.exp(-z))
            curve_list.append((z, y))
            print(z, y)
        for i in range(len(intervals)-1):
            x1 = x_is_min + (x_scale * (curve_list[i][0] + 5)) / 10
            y1 = y_is_0 - curve_list[i][1] * y_scale
            x2 = x_is_min + (x_scale * (curve_list[i+1][0] + 5)) / 10
            y2 = y_is_0 - curve_list[i+1][1] * y_scale
            self.canvas.create_line(x1, y1, x2, y2, width=thickness, fill='black')

        x = self.app.dataset.x[self.app.current_item_index]
        z, y = self.app.network.forward(x)
        z = z[0,0]
        y = y[0,0]
        print(x, z, y)
        print('x1={} + {}*({}+5)'.format(x_is_min, x_scale, z))
        x1 = round(x_is_min + (x_scale*(z+5))/10)
        y1 = round(y_is_0 - y*y_scale)
        x2 = round(x_is_min + (x_scale*(z+5))/10)
        y2 = round(y_is_0 - y*y_scale)
        print((x1, y1), (x2, y2))
        self.canvas.create_line(x1, y_is_0, x2, y_is_0-y_scale, width=thickness, fill='gold')
        self.canvas.create_line(x_is_min, y1, x_is_min+x_scale, y2, width=thickness, fill='gold')

        self.canvas.create_text(x_is_min+x_scale*0.5, y_is_0-y_scale-30, text="y Activation Function", font="Arial 14 bold", fill="#000000")
        self.canvas.create_text(x_is_min+x_scale*0.5, y_is_0-y_scale-15, text="y = 1 / (1 + e^-z)", font="Arial 12 bold",
                                        fill="#000000")
        self.canvas.create_text(x_is_min+x_scale*0.5, y_is_0+10, text="z = 0", font="Arial 11 bold", fill="#000000")
        self.canvas.create_text(x_is_min+x_scale, y_is_0+10, text="z = +5", font="Arial 11 bold", fill="#000000")
        self.canvas.create_text(x_is_min, y_is_0+10, text="z = -5", font="Arial 11 bold", fill="#000000")
        self.canvas.create_text(x_is_min+x_scale*0.5-13, y_is_0-10, text="y=0", font="Arial 11 bold", fill="#000000")
        self.canvas.create_text(x_is_min+x_scale*0.5 - 16, y_is_0 - 0.5*y_scale, text="y=0.5", font="Arial 11 bold", fill="#000000")
        self.canvas.create_text(x_is_min+x_scale*0.5 - 13, y_is_0 - y_scale, text="y=1", font="Arial 11 bold", fill="#000000")
        self.canvas.create_text(x_is_min+x_scale*0.5, y_is_0 + 25, text="z = b0*1 + b1*x1 + b2*x2", font="Arial 11 bold",
                                        fill="#000000")

        b0 = self.app.network.y_bias[0, 0]
        b1 = self.app.network.y_x[0, 0]
        b2 = self.app.network.y_x[0, 1]
        self.canvas.create_text(x_is_min+x_scale*0.5, y_is_0 + 40,
                                        text=f"z = {b0:0.2f}*{1} + {b1:0.2f}*{x[0]} + {b2:0.2f}*{x[1]}",
                                        font="Arial 11 bold",
                                        fill="#000000")
        self.canvas.create_text(x_is_min+x_scale*0.5, y_is_0 + 55,
                                        text="z = {:0.2f} + {:0.2f} + {:0.2f} = {:0.2f}".format(b0, b1*x[0], b2*x[1], z),
                                        font="Arial 11 bold",
                                        fill="#000000")

        self.canvas.create_line(x_is_min+x_scale*0.5, y_is_0, x_is_min+x_scale*0.5, y_is_0-y_scale, width=thickness)
        self.canvas.create_line(x_is_min, y_is_0, x_is_min+x_scale, y_is_0, width=thickness)
