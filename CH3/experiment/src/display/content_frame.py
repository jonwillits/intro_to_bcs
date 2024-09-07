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

        # Place the inner_frame explicitly, initially without height constraints
        self.inner_frame.pack(fill=tk.BOTH, expand=True)

        # Fetch content from content_dict
        if self.frame_name in self.app.content_dict:
            content = self.app.content_dict[self.frame_name]["content"]
        else:
            content = f"No content file for {self.frame_name}"

        # Create the HTML frame with the specified height
        html_frame = markdown_support.create_html_frame(self.inner_frame, content, height)

        # After loading the HTML content, adjust the height based on the content
        self.adjust_inner_frame_height(html_frame)

    def adjust_inner_frame_height(self, html_frame):
        """Adjust the height of the inner_frame based on the content of the HtmlFrame."""
        html_frame.update_idletasks()  # Ensure the HTML frame is fully rendered

        # Get the height of the HTML frame after the content is loaded
        content_height = html_frame.winfo_height()

        print(f"Content height: {content_height}")

        # Set the height of the inner_frame based on the content height
        self.inner_frame.config(height=content_height)



