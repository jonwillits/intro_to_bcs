import tkinter as tk


class ContentFrame:

    def __init__(self, display, frame_name):

        self.display = display
        self.frame = tk.Frame(self.display.content_frame, bg="white")
        self.display.content_frame_dict[frame_name] = self.frame

        self.title_label = tk.Label(self.frame, text=frame_name, font=("Helvetica", 16), bg="white", fg="black")
        self.title_label.place(x=10, y=10)
        self.frame.place(relwidth=1, relheight=1)


class ResizableLabel(tk.Label):
    def __init__(self, parent, text, x=0, y=0, padding=10, **kwargs):
        super().__init__(parent, text=text, **kwargs)
        self.padding = padding

        # Place the label initially, expanding it to fit the parent frame
        self.place(x=x, y=y, relwidth=1, relheight=1)

        # Bind the <Configure> event of the parent to adjust wraplength on resize
        self.bind("<Configure>", self.adjust_wraplength)

    def adjust_wraplength(self, event=None):
        # Calculate the new wraplength based on the current width minus padding
        new_width = self.winfo_width() - 2 * self.padding
        if new_width > 0:
            self.config(wraplength=new_width)
