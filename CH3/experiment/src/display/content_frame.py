import tkinter as tk


class ContentFrame:


    def __init__(self, display, frame_name):

        self.display = display
        self.frame = tk.Frame(self.display.content_frame)
        self.display.content_frame_dict[frame_name] = self.frame

        self.title_label = tk.Label(self.frame, text=frame_name, font=("Helvetica", 16))
        self.title_label.place(x=10, y=10)
        self.frame.place(relwidth=1, relheight=1)

class ResizableLabelFrame(tk.Frame):
    def __init__(self, parent, text, padding=20):
        super().__init__(parent, bg="purple")
        self.padding = padding
        self.text = text
        self.parent = parent
        self.label = None

        # Bind the <Configure> event to adjust the label's size and wraplength
        parent.bind("<Configure>", self.create_label())

        self.create_label()

    def create_label(self, event=None):
        # Get the current width of the parent frame
        print(self.text)
        if self.label is not None:
            self.label.destroy()

        # Create the label
        self.label = tk.Label(self, text=self.text, anchor="nw", justify="left")
        self.label.place(x=self.padding, y=self.padding)
        #
        # parent_width = self.winfo_width()
        # label_width = parent_width - 2 * self.padding
        # self.label.place_configure(width=label_width)
        # self.label.update()
        # self.label.update_idletasks()
        # self.parent.update()
        # self.parent.update_idletasks()



