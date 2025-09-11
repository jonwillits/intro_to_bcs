import tkinter as tk
from tkinterweb import HtmlFrame


class ScrollableHtmlFrame:
    def __init__(self, root):
        self.root = root

        # Create a canvas to allow scrolling
        self.canvas = tk.Canvas(root)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Add a scrollbar
        scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Configure the canvas to work with the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to host the HtmlFrame
        self.inner_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Create an HtmlFrame inside the inner frame
        self.html_frame = HtmlFrame(self.inner_frame, horizontal_scrollbar="auto")
        self.html_frame.pack(expand=True, fill="both")

        # Sample HTML content
        html_content = """
        <h1>Title</h1>
        <p>This is a paragraph with some <strong>bold</strong> and <em>italic</em> text.</p>
        <p>Here is some more content that should cause the frame to expand based on the length of this text.</p>
        <p>More content here... to test scrolling!</p>
        """

        # Use load_html() to set HTML content in HtmlFrame
        self.html_frame.load_html(html_content)

        # Bind the canvas resize event to update the scroll region
        self.inner_frame.bind("<Configure>", self.on_frame_configure)

    def on_frame_configure(self, event):
        """Adjust the scrollable area based on the inner frame content size."""
        # Update the scroll region to encompass the whole inner frame (including content not visible)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


# Main app setup
root = tk.Tk()
app = ScrollableHtmlFrame(root)
root.geometry("600x400")
root.mainloop()
