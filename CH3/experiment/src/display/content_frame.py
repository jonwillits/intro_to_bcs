import tkinter as tk
from tkinter import scrolledtext
from . import markdown_support


class ContentFrame:

    def __init__(self, display, frame_name):

        self.display = display
        self.frame_name = frame_name

        # Set the parent as the canvas from the display
        self.inner_frame = tk.Frame(self.display.main_frame_canvas, bg="white")

        if self.frame_name in self.display.content_dict:
            ext = self.display.content_dict[self.frame_name]["file_extension"]

            if ext == 'txt':
                content = self.display.content_dict[self.frame_name]["content"]


            elif ext == 'md':
                content = self.display.content_dict[self.frame_name]["content"]

            else:
                content = f"Unrecognized content file type {ext} for {self.frame_name}"

        else:
            content = f"No content file for {self.frame_name}"

        text_widget = self.create_text_widget()
        converter = markdown_support.MarkdownToTkinter(text_widget)
        converter.convert_markdown_to_tkinter(content)

        self.inner_frame.bind("<Configure>", self.adjust_wrap_length)

        # Call geometry update
        self.inner_frame.update()
        self.inner_frame.update_idletasks()

    def create_text_widget(self, height=None, width=None):
        if height is None:
            height = self.display.main_frame_dimensions[0]
        if width is None:
            width = self.display.main_frame_dimensions[1]

        text_widget = scrolledtext.ScrolledText(self.inner_frame, wrap=tk.WORD,
                                                height=height,
                                                width=width,
                                                bg="white",
                                                fg="black")
        text_widget.pack(expand=True, fill='both')
        text_widget.tag_configure('heading1', font=('Helvetica', 16, 'bold'))
        text_widget.tag_configure('heading2', font=('Helvetica', 14, 'bold'))
        text_widget.tag_configure('bold', font=('Helvetica', 12, 'bold'))
        text_widget.tag_configure('italic', font=('Helvetica', 12, 'italic'))
        return text_widget

    def adjust_wrap_length(self, event=None):
        pass
        # # Handle case where event is None (when method is called manually)
        # if event:
        #     new_width = event.width - 20  # Subtracting padding if needed
        # else:
        #     new_width = self.inner_frame.winfo_width() - 20  # Use current width if no event
        #
        # # Ensure that the new_width is positive before applying it
        # if new_width > 0:
        #     self.content_label.config(wraplength=new_width)