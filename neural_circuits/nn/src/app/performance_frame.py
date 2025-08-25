import tkinter as tk
import math
import numpy as np

class PerformanceFrame:

    def __init__(self, app, x, y, height, width):
        self.app = app
        self.frame = tk.Frame(app.main_frame, bg="blue", height=height, width=width)
        self.frame.place(x=x, y=y)
        self.canvas = tk.Canvas(self.frame, bg="#BBBBBB", height=height, width=width, borderwidth=0, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def draw_frame(self):
        self.canvas.delete("all")
        start_x = 50
        start_y = 10
        button_height = 32
        button_width = 60
        self.canvas.create_text(start_x, start_y, text="Performance:", font="Arial 16 bold", fill="#000000")