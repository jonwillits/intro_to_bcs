import tkinter as tk

class ClassificationFrame:
    def __init__(self, app, x, y, height, width):
        self.app = app
        self.frame = tk.Frame(app.main_frame, bg="blue", height=height, width=width)
        self.frame.place(x=x, y=y)
        self.canvas = tk.Canvas(self.frame, bg="#BBBBBB", height=height, width=width, borderwidth=0, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.thickness = 3

    def find_decision_boundary(self, x_val):
        precision = 0.01
        y = -100
        n = 100
        y_predict = 0
        while abs(y_predict - 0.50) > precision:
            z, y_predict = self.app.network.forward([x_val, y])
            y += 1 / n
            if y > 100:
                break
        return y

    def draw_frame(self):
        self.canvas.delete("all")
        start_x = 0
        start_y = 0
        self.canvas.create_text(start_x + 10, start_y + 10, text="Decision Boundary:", font="Arial 16 bold",
                                fill="#000000", anchor="nw")

        x_is_0 = 50  # X origin on canvas
        y_is_0 = 150  # Y origin on canvas
        scale = 100  # Scaling factor for drawing

        # Find y-values for the decision boundary at x=0 and x=1
        y1 = self.find_decision_boundary(0)
        y2 = self.find_decision_boundary(1)

        # Calculate slope and intercept
        m = (y2 - y1)  # Slope
        b = y1         # Intercept

        # Calculate the points of the line on the canvas
        x1_canvas = x_is_0
        y1_canvas = y_is_0 - scale * y1
        x2_canvas = x_is_0 + scale  # x2 is x=1 on the canvas
        y2_canvas = y_is_0 - scale * y2

        # Draw the decision boundary line
        self.canvas.create_line(x1_canvas, y1_canvas, x2_canvas, y2_canvas, width=self.thickness, fill='yellow')

        # Draw dataset points
        for i in range(self.app.dataset.n):
            x1 = self.app.dataset.x[i][0]
            x2 = self.app.dataset.x[i][1]
            y = self.app.dataset.y[i][0]
            print(x1, x2, y)
            color = 'green' if y == 1 else 'red'

            # Draw the point as an oval
            self.canvas.create_oval(x_is_0 + scale * x1 - 4,
                                    y_is_0 - scale * x2 - 4,
                                    x_is_0 + scale * x1 + 4,
                                    y_is_0 - scale * x2 + 4,
                                    fill=color)

            # Add a label for the point
            label = "({}, {})".format(x1, x2)
            self.canvas.create_text(x_is_0 + scale * x1, y_is_0 - scale * x2 - 10, text=label, font="Arial 12", fill="#000000")
