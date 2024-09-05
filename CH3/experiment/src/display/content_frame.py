import tkinter as tk


class ContentFrame:

    def __init__(self, display, frame_name):

        self.display = display
        self.frame_name = frame_name

        # Set the parent as the canvas from the display
        self.inner_frame = tk.Frame(self.display.main_frame_canvas, bg="white")

        if self.frame_name in self.display.content_dict:
            content = self.display.content_dict[self.frame_name]["content"]
        else:
            content = f"No content for {self.frame_name}"

        self.content_label = tk.Label(self.inner_frame,
                                    text=content,
                                    font=("Helvetica", 16),
                                    bg="white",
                                    justify="left",
                                    fg="black")

        # Use pack() instead of place() for dynamic resizing
        self.content_label.pack(padx=10, pady=10, anchor="nw", fill="both")

        self.inner_frame.bind("<Configure>", self.adjust_wrap_length)

        # Call geometry update
        self.inner_frame.update()
        self.inner_frame.update_idletasks()


    def adjust_wrap_length(self, event=None):
        # Handle case where event is None (when method is called manually)
        if event:
            new_width = event.width - 20  # Subtracting padding if needed
        else:
            new_width = self.inner_frame.winfo_width() - 20  # Use current width if no event

        # Ensure that the new_width is positive before applying it
        if new_width > 0:
            self.content_label.config(wraplength=new_width)