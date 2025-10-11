import os.path
import tkinter as tk
from pathlib import Path
from . import content_frame
from . import section_menu_frame
from . import markdown_support

class App:
    def __init__(self, the_params):
        self.the_params = the_params
        self.window_dimensions = (the_params.width, the_params.height)
        self.min_dimensions = (950, 600)
        self.section_menu_frame_dimensions = (150, self.window_dimensions[1])
        self.section_content_frame_dimensions = (self.window_dimensions[0] - self.section_menu_frame_dimensions[0],
                                      self.window_dimensions[1])


        self.root = None
        self.section_menu_frame = None

        self.section_content_frame = None
        self.section_content_canvas = None
        self.section_content_canvas_scrollbar = None
        self.content_frame_dict = None

        self.current_canvas_window = None
        self.current_content_frame = None

        self.load_section_content()
        self.create_main_window()
        self.create_section_menu_frame()
        self.create_section_content_frame()

    @staticmethod
    def load_content_file(file_path, color):
        file_extension = Path(file_path).suffix[1:]
        with open(file_path, 'r', encoding='utf-8') as f:
            file_contents = f.read()
        if file_extension == "md":
            file_contents = markdown_support.convert_markdown_to_html(file_contents, bg_color=color)
        elif file_extension == 'txt':
            file_contents = file_contents
        elif file_extension == 'html':
            file_contents = file_contents
        else:
            raise Exception(f"ERROR: Unrecognized content file type {file_extension} for {file_path}")
        return file_contents

    def load_section_content(self):
        for i, section_info in enumerate(self.the_params.section_list):
            component_list = section_info['components']
            color_list = ['pink', 'cyan', 'tan', 'lightgrey', 'yellow', 'magenta']
            for j, component in enumerate(component_list):
                component_file_name = component['file_name']
                component_file_path = os.path.join(self.the_params.content_path, component_file_name)
                file_contents = self.load_content_file(component_file_path, color_list[j])
                self.the_params.section_list[i]['components'][j]['content'] = file_contents

    def create_main_window(self):
        self.root = tk.Tk()
        self.root.geometry(f"{self.window_dimensions[0]}x{self.window_dimensions[1]}")
        self.root.title("Experiment Simulation")
        self.root.minsize(self.min_dimensions[0], self.min_dimensions[1])

    def create_section_menu_frame(self):
        self.section_menu_frame = section_menu_frame.SectionMenuFrame(self)
        self.section_menu_frame.section_menu_frame.pack(side="left", fill="y", expand=False)  # Allow vertical expansion

    def update_scroll_region(self, event=None):
        """Update the canvas scroll region to ensure it fits the entire content frame."""
        bbox = self.section_content_canvas.bbox("all")  # Bounding box of all elements in the canvas
        print(f"Bounding box of all elements: {bbox}")  # For debugging
        self.section_content_canvas.configure(scrollregion=bbox)  # Update scroll region

    def create_section_content_frame(self):
        # Create a frame that holds both the canvas and the scrollbar
        self.section_content_frame = tk.Frame(self.root,
                                              borderwidth=2,
                                              highlightbackground="black",
                                              highlightthickness=2,
                                              relief="solid",
                                              bg="red")
        self.section_content_frame.pack(side="right", fill="both", expand=True)  # Allow horizontal and vertical expansion

        # Create a canvas for the main content area inside the canvas_frame
        self.section_content_canvas = tk.Canvas(self.section_content_frame,
                                           highlightbackground="white",
                                           highlightthickness=0,
                                           borderwidth=0,
                                           relief="solid",
                                           bg="blue")
        self.section_content_canvas.pack(side="left", fill="both", expand=True)

        # Add a vertical scrollbar inside the canvas_frame (on the right)
        self.section_content_canvas_scrollbar = tk.Scrollbar(self.section_content_frame,
                                                             orient="vertical",
                                                             command=self.section_content_canvas.yview)
        self.section_content_canvas_scrollbar.pack(side="right", fill="y")

        # Connect the scrollbar with the canvas
        self.section_content_canvas.configure(yscrollcommand=self.section_content_canvas_scrollbar.set)

        # Initialize an empty content frame dict (frames will be created dynamically)
        self.content_frame_dict = {}

        # Ensure the canvas updates its scroll region when resized
        self.section_content_canvas.bind("<Configure>", self.update_scroll_region)

        # Show the first frame by default
        self.show_section(0)

    def show_section(self, index):
        section_content = self.the_params.section_list[index]
        title = section_content['title']

        if self.current_canvas_window is not None:
            self.section_content_canvas.delete(self.current_canvas_window)

        if not 'frame' in section_content:
            content_frame_instance = content_frame.ContentFrame(self, section_content)
        else:
            content_frame_instance = section_content['frame']
        print(f"Showing section: {title}")

        # Use create_window() to place the new frame in the canvas
        self.current_canvas_window = self.section_content_canvas.create_window(
            (0, 0), window=content_frame_instance.frame, anchor="nw", width=self.section_content_canvas.winfo_width())

        # Force geometry update
        self.section_content_canvas.update_idletasks()

        # Update the scroll region after the frame is shown
        self.update_scroll_region()

        # Bind the canvas resizing event to adjust the content frame width dynamically
        self.section_content_canvas.bind("<Configure>", self.update_content_frame_width)

    def update_content_frame_width(self, event=None):
        """Ensure the content frame width matches the canvas width during resize."""
        if self.current_canvas_window is not None:
            canvas_width = event.width if event else self.main_frame_canvas.winfo_width()
            print(f"Resizing content to width: {canvas_width}")
            self.main_frame_canvas.itemconfig(self.current_canvas_window, width=canvas_width)

            # Ensure the scroll region is updated
            self.update_scroll_region()

    def quit(self):
        self.root.quit()
