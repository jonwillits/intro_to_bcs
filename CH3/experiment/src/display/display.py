import tkinter as tk
from pathlib import Path
from . import content_frame

class Display:
    def __init__(self, the_experiment, section_list, content_dict, width=950, height=600):
        self.the_experiment = the_experiment
        self.section_list = section_list
        self.content_dict = content_dict
        self.window_dimensions = (width, height)
        self.root = None
        self.min_dimensions = (1, 1)

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

    def create_main_window(self):
        self.root = tk.Tk()
        self.root.geometry(f"{self.window_dimensions[0]}x{self.window_dimensions[1]}")
        self.root.title("Experiment Simulation")
        self.root.minsize(self.min_dimensions[0], self.min_dimensions[1])

    def create_section_frame(self):
        self.section_frame = tk.Frame(self.root, bg="#707372", width=self.section_frame_dimensions[0])
        self.section_frame.pack(side="left", fill="y")

        for i, section in enumerate(self.section_list):
            base_name = Path(section).stem
            if base_name in self.content_dict:
                content = self.content_dict[base_name]['content']

                if content.startswith("# "):
                    title = f"{i + 1}. {content[2:].split('\n', 1)[0]}"
                else:
                    title = f"{i + 1}. {base_name}"

                button = tk.Button(self.section_frame,
                                   anchor="w",
                                   text=title,
                                   fg="black",
                                   bg="#FF5F05",
                                   font=("Helvetica", 10),
                                   command=lambda name=base_name: self.show_frame(name),
                                   height=1,
                                   padx=2,
                                   pady=2,
                                   borderwidth=2,
                                   highlightthickness=1,
                                   relief="flat")
                button.pack(side="top", fill="x", pady=1)

    def update_scroll_region(self, event=None):
        """Update the canvas scroll region to ensure it fits the entire content frame."""
        bbox = self.main_frame_canvas.bbox("all")  # Bounding box of all elements in the canvas
        self.main_frame_canvas.configure(scrollregion=bbox)

    def create_main_frame(self):
        # Create a frame that holds both the canvas and the scrollbar
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(side="right", fill="both", expand=True)

        # Create a canvas for the main content area inside the canvas_frame
        self.main_frame_canvas = tk.Canvas(self.canvas_frame, bg="white")
        self.main_frame_canvas.pack(side="left", fill="both", expand=True)

        # Add a vertical scrollbar inside the canvas_frame (on the right)
        self.main_frame_canvas_scrollbar = tk.Scrollbar(self.canvas_frame,
                                                        orient="vertical",
                                                        command=self.main_frame_canvas.yview)
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
            content_frame_instance = content_frame.ContentFrame(self, frame_name)
            self.content_frame_dict[frame_name] = content_frame_instance
        else:
            content_frame_instance = self.content_frame_dict[frame_name]

        # Use create_window() to place the new frame in the canvas
        self.current_canvas_window = self.main_frame_canvas.create_window(
            (0, 0), window=content_frame_instance.inner_frame, anchor="nw", width=self.main_frame_canvas.winfo_width()
        )

        # Force geometry update
        self.main_frame_canvas.update_idletasks()
        self.main_frame_canvas.update()

        # Update the scroll region after the frame is shown
        self.update_scroll_region()

        # Print debug information for the displayed frame
        bbox = self.main_frame_canvas.bbox("all")
        canvas_width = self.main_frame_canvas.winfo_width()
        canvas_height = self.main_frame_canvas.winfo_height()

        inner_frame_width = self.content_frame_dict[frame_name].inner_frame.winfo_width()
        inner_frame_height = self.content_frame_dict[frame_name].inner_frame.winfo_height()

        print(f"Current Canvas Size: ({canvas_width},{canvas_height})")
        print(f"Current bbox: {bbox}")
        print(f"Current Inner Frame Size: ({inner_frame_width},{inner_frame_height})")



