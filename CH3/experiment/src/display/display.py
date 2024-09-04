import tkinter as tk
from . import content_frame
from . import overview_frame

class Display:
    def __init__(self, the_experiment, content_dict, width=950, height=600):

        self.the_experiment = the_experiment
        self.content_dict = content_dict
        self.window_dimensions = (width, height)
        self.root = None
        self.min_dimensions = (950, 600)

        self.tab_frame = None
        self.tab_frame_dimensions = (150, self.window_dimensions[1])
        self.tabs_dict = None
        self.tab_button_width = 0
        self.tab_button_padding = 0
        self.tab_button_height = 2

        self.main_frame = None
        self.main_frame_dimensions = (self.window_dimensions[0]-self.tab_frame_dimensions[0], self.window_dimensions[1])

        self.content_frame = None
        self.content_frame_dimensions = None
        self.content_frame_dict = None

        self.create_main_window()
        self.create_tab_frame()
        self.create_main_frame()

    def create_main_window(self):
        self.root = tk.Tk()
        self.root.geometry(f"{self.window_dimensions[0]}x{self.window_dimensions[1]}")
        self.root.title("Experiment Simulation")
        self.root.minsize(self.min_dimensions[0], self.min_dimensions[1])

    def resize_display(self, event=None):
        pass

    def create_tab_frame(self):
        self.tab_frame = tk.Frame(self.root, bg="#3C3C3E", width=self.tab_frame_dimensions[0])
        self.tab_frame.pack(side="left", fill="y")
        self.tabs_dict = {}

        for key, value in self.content_dict.items():
            if value[0] == "#":
                button = tk.Button(self.tab_frame,
                                   text=key,
                                   fg="black",
                                   bg="lightgrey",
                                   font=("Helvetica", 12),
                                   command=lambda name=key: self.show_frame(name),
                                   width=self.tab_button_width,
                                   height=self.tab_button_height,
                                   padx=self.tab_button_padding,
                                   pady=self.tab_button_padding,
                                   borderwidth=1,
                                   highlightthickness=1,
                                   relief="flat")
                button.pack(side="left")
                self.tabs_dict[key] = button

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root, bg="black")
        self.main_frame.pack(side="left", expand=True, fill="both")
        
        self.content_frame = tk.Frame(self.main_frame, bg="white")
        self.content_frame.pack(side="bottom", expand=True, fill="both")

        self.content_frame_dict = {}

        overview_frame.OverviewFrame(self, "Overview")
        content_frame.ContentFrame(self, "Population")
        content_frame.ContentFrame(self, "Current Experiment")
        content_frame.ContentFrame(self, "Experiment History")


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



        # Show the default frame
        self.show_frame("overview")

    def show_frame(self, frame_name):
        self.content_frame_dict[frame_name].tkraise()



