import tkinter as tk
from . import options_frame
from . import content_frame
from . import overview_frame

class Display:
    def __init__(self, the_experiment, content_dict, width=950, height=600):

        self.the_experiment = the_experiment
        self.content_dict = content_dict
        self.window_dimensions = (width, height)
        self.root = None
        self.min_dimensions = (950, 600)

        self.main_frame = None
        self.main_frame_dimensions = None

        self.tab_frame = None
        self.tab_frame_dimensions = None
        self.tabs_dict = None
        self.tab_button_width = 0
        self.tab_button_padding = 0
        self.tab_button_height = 2

        self.content_frame = None
        self.content_frame_dimensions = None
        self.content_frame_dict = None

        self.create_main_window()
        # self.the_options_frame = options_frame.OptionsFrame(self)
        self.create_tab_frame()
        self.create_main_frame()

    def create_main_window(self):
        self.root = tk.Tk()
        self.root.geometry(f"{self.window_dimensions[0]}x{self.window_dimensions[1]}")
        self.root.title("Experiment Simulation")
        self.root.minsize(self.min_dimensions[0], self.min_dimensions[1])

    def resize_display(self, event=None):
        pass
        # self.the_options_frame.resize()


    def create_tab_frame(self):
        self.tab_frame = tk.Frame(self.root, bg="#3C3C3E")
        self.tab_frame.pack(side="top", fill="x")

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root, bg="black")
        self.main_frame.pack(side="right", expand=True, fill="both")
        
        self.content_frame = tk.Frame(self.main_frame, bg="white")
        self.content_frame.pack(side="bottom", expand=True, fill="both")

        self.content_frame_dict = {}

        overview_frame.OverviewFrame(self, "Overview")
        content_frame.ContentFrame(self, "Population")
        content_frame.ContentFrame(self, "Current Experiment")
        content_frame.ContentFrame(self, "Experiment History")

        self.tabs_dict = {}

        for content_frame_name in self.content_frame_dict:
            button = tk.Button(self.tab_frame,
                               text=content_frame_name,
                               fg="black",
                               bg="lightgrey",
                               font=("Helvetica", 12),
                               command=lambda name=content_frame_name: self.show_frame(name),  # will this work, with the function passed in as a string?
                               width=self.tab_button_width,
                               height=self.tab_button_height,
                               padx=self.tab_button_padding,
                               pady=self.tab_button_padding,
                               borderwidth=1,
                               highlightthickness=1,
                               relief="flat")

            # button = tk.Button(self.tab_frame,
            #                    text=content_frame_name,
            #                    command=lambda name=content_frame_name: self.show_frame(name),
            #                    highlightbackground="darkslategray",
            #                    bg="lightgrey"
            #                    # Capture the current content_frame_name
            # )
            button.pack(side="left")
            self.tabs_dict[content_frame_name] = button

        # Show the default frame
        self.show_frame("Overview")

    def show_frame(self, frame_name):
        self.content_frame_dict[frame_name].tkraise()



