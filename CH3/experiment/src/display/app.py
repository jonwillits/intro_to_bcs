import tkinter as tk
from pathlib import Path
from . import content_frame
from . import section_frame

class App:
    def __init__(self, the_experiment, section_list, content_dict, width=950, height=600):
        self.the_experiment = the_experiment
        self.section_list = section_list
        self.content_dict = content_dict
        self.window_dimensions = (width, height)
        self.root = None
        self.min_dimensions = (950, 600)

        self.section_frame = None
        self.section_frame_dimensions = (150, self.window_dimensions[1])

        self.main_frame_dimensions = (self.window_dimensions[0] - self.section_frame_dimensions[0],
                                      self.window_dimensions[1])

        self.main_frame_canvas = None
        self.main_frame_canvas_scrollbar = None
        self.content_frame_dict = {}
        self.canvas_frame = None
        self.current_canvas_window = None
        self.current_content_frame = None

        self.create_main_window()
        self.create_section_frame()
        self.create_main_frame()
        self.root.update_idletasks()
        print(self.root.winfo_width(), self.root.winfo_height())

    def create_main_window(self):
        self.root = tk.Tk()
        self.root.geometry(f"{self.window_dimensions[0]}x{self.window_dimensions[1]}")
        self.root.title("Experiment Simulation")
        self.root.minsize(self.min_dimensions[0], self.min_dimensions[1])

    def create_section_frame(self):
        self.section_frame = section_frame.SectionFrame(self)
        self.section_frame.section_frame.pack(side="left", fill="y", expand=False)  # Allow vertical expansion

    def update_scroll_region(self, event=None):
        """Update the canvas scroll region to ensure it fits the entire content frame."""
        bbox = self.main_frame_canvas.bbox("all")  # Bounding box of all elements in the canvas
        self.main_frame_canvas.configure(scrollregion=bbox)

    def create_main_frame(self):
        # Create a frame that holds both the canvas and the scrollbar
        self.canvas_frame = tk.Frame(self.root,
                                     borderwidth=2,
                                     highlightbackground="black",
                                     highlightthickness=2,
                                     relief="solid",
                                     bg="white")
        self.canvas_frame.pack(side="right", fill="both", expand=True)  # Allow horizontal and vertical expansion

        # Create a canvas for the main content area inside the canvas_frame
        self.main_frame_canvas = tk.Canvas(self.canvas_frame,
                                           highlightbackground="white",
                                           highlightthickness=0,
                                           borderwidth=0,
                                           relief="solid",
                                           bg="white")
        self.main_frame_canvas.pack(side="left", fill="both", expand=True)

        # Add a vertical scrollbar inside the canvas_frame (on the right)
        self.main_frame_canvas_scrollbar = tk.Scrollbar(self.canvas_frame, orient="vertical", command=self.main_frame_canvas.yview)
        self.main_frame_canvas_scrollbar.pack(side="right", fill="y")

        # Connect the scrollbar with the canvas
        self.main_frame_canvas.configure(yscrollcommand=self.main_frame_canvas_scrollbar.set)

        # Initialize an empty content frame dict (frames will be created dynamically)
        self.content_frame_dict = {}

        # Ensure the canvas updates its scroll region when resized
        self.main_frame_canvas.bind("<Configure>", self.update_scroll_region)

        # Show the first frame by default
        self.show_frame(Path(self.section_list[0]).stem)

    def show_frame(self, frame_name):
        print(f"Showing frame: {frame_name}")

        # Remove the previous frame from the canvas
        if self.current_canvas_window is not None:
            self.main_frame_canvas.delete(self.current_canvas_window)

        # Dynamically create the content frame only if it doesn't already exist
        if frame_name not in self.content_frame_dict:
            content_frame_instance = content_frame.ContentFrame(self, frame_name, 100)
            self.content_frame_dict[frame_name] = content_frame_instance
        else:
            content_frame_instance = self.content_frame_dict[frame_name]

        # Ensure the content frame fills the width of the canvas
        canvas_width = self.main_frame_canvas.winfo_width()

        # Use create_window() to place the new frame in the canvas
        self.current_canvas_window = self.main_frame_canvas.create_window((0, 0), window=content_frame_instance.inner_frame, anchor="nw", width=canvas_width)

        # Force geometry update
        self.main_frame_canvas.update_idletasks()

        # Update the scroll region after the frame is shown
        self.update_scroll_region()

        # Bind the canvas resizing event to adjust the content frame width dynamically
        self.main_frame_canvas.bind("<Configure>", self.update_content_frame_width)

    def update_content_frame_width(self, event=None):
        """Ensure the content frame width matches the canvas width."""
        if self.current_canvas_window is not None:
            canvas_width = event.width if event else self.main_frame_canvas.winfo_width()
            self.main_frame_canvas.itemconfig(self.current_canvas_window, width=canvas_width)

    def quit(self):
        self.root.quit()
