import os.path
import tkinter as tk
from pathlib import Path
from . import content_frame
from . import section_frame
from . import markdown_support

class App:
    def __init__(self, the_params):
        self.the_params = the_params
        self.window_dimensions = (the_params.width, the_params.height)
        self.min_dimensions = (950, 600)
        self.section_frame_dimensions = (150, self.window_dimensions[1])
        self.main_frame_dimensions = (self.window_dimensions[0] - self.section_frame_dimensions[0],
                                      self.window_dimensions[1])

        self.root = None

        self.section_frame = None
        self.section_content_list = None

        self.main_frame_canvas = None
        self.main_frame_canvas_scrollbar = None
        self.content_frame_dict = None
        self.canvas_frame = None
        self.current_canvas_window = None
        self.current_content_frame = None

        self.load_section_content()
        self.create_main_window()
        self.create_section_frame()
        self.create_main_frame()

    def load_section_content(self):
        self.section_content_list = []
        for i, section_info in enumerate(self.the_params.section_list):
            component_list = section_info['components']

            for j, component in enumerate(component_list):
                component_file_name = component[0]
                component_file_path = os.path.join(self.the_params.content_path, component_file_name)
                file_contents = markdown_support.load_content(component_file_path)
                self.the_params.section_list[i]['components'][j]['content'] = file_contents

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
                                     bg="red")
        self.canvas_frame.pack(side="right", fill="both", expand=True)  # Allow horizontal and vertical expansion

        # Create a canvas for the main content area inside the canvas_frame
        self.main_frame_canvas = tk.Canvas(self.canvas_frame,
                                           highlightbackground="white",
                                           highlightthickness=0,
                                           borderwidth=0,
                                           relief="solid",
                                           bg="blue")
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
        self.show_section(Path(self.section_list[0]).stem)

    def show_section(self, section_name):
        print(f"Showing frame: {frame_name}")

        # Remove the previous frame from the canvas
        if self.current_canvas_window is not None:
            self.main_frame_canvas.delete(self.current_canvas_window)

        # Dynamically create the content frame only if it doesn't already exist
        if frame_name not in self.content_frame_dict:
            content_frame_instance = content_frame.ContentFrame(self, frame_name, 1200)
            self.content_frame_dict[frame_name] = content_frame_instance
        else:
            content_frame_instance = self.content_frame_dict[frame_name]

        # Ensure the content frame fills the width of the canvas
        canvas_width = self.main_frame_canvas.winfo_width()

        # Use create_window() to place the new frame in the canvas
        self.current_canvas_window = self.main_frame_canvas.create_window((0, 0),
                                                                          window=content_frame_instance.inner_frame,
                                                                          anchor="nw",
                                                                          width=canvas_width)

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
