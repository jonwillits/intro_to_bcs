import tkinter as tk

class App:

    def __init__(self, app_dimensions, training_set, test_set, network):
        self.app_dimensions = app_dimensions
        self.training_set = training_set
        self.test_set = test_set
        self.network = network

        self.root = None

        self.create_main_window()


    def create_main_window(self):

        self.root = tk.Tk()
        self.root.geometry(f'{self.app_dimensions[0]}x{self.app_dimensions[1]}')
        # change the title to "Neural Network Simulator"