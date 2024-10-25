import tkinter as tk
from . import interface_frame
from . import network_frame

class App:

    def __init__(self, network, dataset):

        self.network = network
        self.dataset = dataset
        self.root = None

        self.app_dimensions = (1100, 650)

        self.interface_frame = None
        self.current_shape_label = None
        self.shape_instance_entry = None
        self.show_instance_button = None

        self.main_frame = None
        self.network_frame = None

        self.create_app_window()
        self.displayed_current_instance_index = tk.IntVar(value=0)
        self.current_instance_index = 0
        self.create_interface_frame()
        self.create_main_frame()

    def create_app_window(self):
        self.root = tk.Tk()
        self.root.title("Shape Classifier")
        self.root.geometry(f"{self.app_dimensions[0]}x{self.app_dimensions[1]}")
        self.root.config(bg="black")
        self.root.update()

    def create_interface_frame(self):
        self.interface_frame = interface_frame.InterfaceFrame(self, self.root)
        self.interface_frame.frame.pack(side=tk.TOP, fill=tk.X)

    def create_main_frame(self):
        # Main frame
        self.main_frame = tk.Frame(self.root, bg="#4574a3", width=self.app_dimensions[0])
        self.main_frame.pack_propagate(False)
        self.main_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        self.create_network_frame()

    def create_network_frame(self):
        self.network_frame = network_frame.NetworkFrame(self, self.main_frame)
        self.network_frame.frame.place(x=5, y=5)