import tkinter as tk
from . import markdown_support

class ContentFrame:

    def __init__(self, app, frame_name, height):
        self.app = app
        self.frame_name = frame_name

        # Set the parent as the canvas from the display
        self.inner_frame = tk.Frame(self.app.main_frame_canvas,
                                    highlightbackground="white",
                                    highlightthickness=0,
                                    borderwidth=0,
                                    bg="white")

        # Fetch content from content_dict
        if self.frame_name in self.app.content_dict:
            content = self.app.content_dict[self.frame_name]["content"]
        else:
            content = f"No content file for {self.frame_name}"


        self.inner_frame.update()
        self.inner_frame.update_idletasks()

        # Adjust the height of the text widget based on the content size

        markdown_support.create_html_frame(self.inner_frame, content, height)

