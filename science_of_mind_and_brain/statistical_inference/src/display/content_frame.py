import tkinter as tk
from tkinterweb import HtmlLabel
from pathlib import Path

class ContentFrame:

    def __init__(self, app, content):
        self.app = app
        self.title = content['title']
        self.component_list = content['components']
        self.frame = None
        self.total_height = 0  # Track total height dynamically

        self.create_frame()

    def create_frame(self):
        # Create the frame that holds the HTML content
        self.frame = tk.Frame(self.app.main_frame_canvas,
                              highlightbackground="white",
                              highlightthickness=0,
                              borderwidth=0,
                              bg="white")
        self.frame.pack(fill=tk.X)

        # Iterate over components and add HTML content
        for i, component in enumerate(self.component_list):
            file_name = component['file_name']
            file_extension = Path(file_name).suffix[1:]

            if file_extension == 'py':
                pass  # Skip Python components
            else:
                if 'content' in component:
                    content = component['content']
                    self.add_html_label(content)
                else:
                    raise Exception(f"ERROR: No content for component {self.title}-{file_name}")

        # Bind the resize event to handle window resizing dynamically
        self.app.section_content_canvas.bind("<Configure>", self.on_resize)

    def add_html_label(self, content):
        # Create the HtmlLabel and load the content
        html_label = HtmlLabel(self.frame, messages_enabled=False, borderwidth=0)
        html_label.load_html(content)

        # Pack the HtmlLabel
        html_label.pack(side="top", fill="x", expand=True)

        # Force the layout update and measure the height
        html_label.update_idletasks()  # Ensure layout updates are processed

        # Get the height of the label and add it to the total height
        label_height = html_label.winfo_height()
        self.total_height += label_height  # Accumulate total height

        # Print for debugging
        print(f"Added HTML Label with height: {label_height}, Total height: {self.total_height}")

        return html_label

    def on_resize(self, event):
        """Handle window resizing and adjust the content dynamically."""
        canvas_width = event.width
        self.app.main_frame_canvas.itemconfig(self.app.current_canvas_window, width=canvas_width)

        # Recalculate total height (optional, if height adjustment is needed)
        self.total_height = sum(child.winfo_height() for child in self.frame.winfo_children())
        print(f"Resized Canvas - New Width: {canvas_width}, Total Height: {self.total_height}")

        # Adjust the scroll region to the new total height
        self.app.main_frame_canvas.config(scrollregion=(0, 0, canvas_width, self.total_height))
