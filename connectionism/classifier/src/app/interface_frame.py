import tkinter as tk
import numpy as np

class InterfaceFrame:

    def __init__(self, app, parent, params):

        self.app = app
        self.parent = parent
        self.params = params

        self.height = 30
        self.width = parent.winfo_width()

        self.frame = None
        self.next_instance_button = None
        self.num_epochs_label =None
        self.num_epochs_entry = None
        self.train_button = None
        self.reset_button = None
        self.clear_canvas_button = None
        self.category_list = params.Shapes.category_list

        # Variable to hold the selected item from the drop-down
        self.category_menu = None
        self.current_category = self.category_list[0]
        self.selected_category_stringvar = tk.StringVar()
        self.selected_category_stringvar.set(self.current_category)
        self.selected_category_stringvar.trace("w", self.on_category_selected)
        self.selected_category_index_list = self.app.training_set.category_index_list_dict[self.current_category]
        self.current_instance_index = 0

        self.create_frame()
        self.add_widgets()

    def create_frame(self):
        self.frame = tk.Frame(self.parent, bg="#222222",
                 height=self.height, width=self.width)
        self.frame.pack_propagate(False)

    def add_widgets(self):
        # Add the entry widget
        self.category_menu = tk.OptionMenu(self.frame, self.selected_category_stringvar, *self.category_list)
        self.category_menu.config(width=10)  # Adjust width as needed
        self.category_menu.pack(side=tk.LEFT, padx=10, pady=5)

        self.next_instance_button = tk.Button(self.frame, text="Next Shape", command=self.increment_instance)
        self.next_instance_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.clear_canvas_button = tk.Button(self.frame, text="Clear Input", command=self.clear_canvas)
        self.clear_canvas_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.num_epochs_label = tk.Label(self.frame, text="Num Epochs", fg="white", bg="#222222")
        self.num_epochs_label.pack(side=tk.LEFT, padx=5, pady=5)

        self.num_epochs_entry = tk.Entry(self.frame, textvariable=self.app.num_epochs, width=10)
        self.num_epochs_entry.pack(side=tk.LEFT, padx=10, pady=5)
        self.num_epochs_entry.insert(0, self.app.num_epochs)

        self.train_button = tk.Button(self.frame, text="Train!", command=self.train)
        self.train_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.reset_button =  tk.Button(self.frame, text="Reset Network", command=self.reset_network)
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=5)

    def train(self):
        self.app.num_epochs_intvar.set(int(self.num_epochs_entry.get()))
        self.app.num_epochs = self.app.num_epochs_intvar.get()
        for i in range(self.app.num_epochs):
            self.app.network.train(self.app.training_set, self.params.Network.learning_rate, self.params.Network.batch_size,
                                   self.app.test_set)
            self.app.network_frame.update_network_frame()

    def on_category_selected(self, *args):
        # This function will be called whenever a new category is selected
        self.current_instance_index = 0
        self.current_category = self.selected_category_stringvar.get()
        self.selected_category_index_list = self.app.training_set.category_index_list_dict[self.current_category]
        x_index = self.selected_category_index_list[self.current_instance_index]
        x = self.app.training_set.x_list[x_index]
        self.app.network_frame.input_frame.set_current_input(x)
        self.app.network_frame.update_network_frame()

    def increment_instance(self):
        self.current_instance_index += 1
        if (self.current_instance_index + 1) == len(self.selected_category_index_list):
            self.current_instance_index = 0
        x_index = self.selected_category_index_list[self.current_instance_index]
        x = self.app.training_set.x_list[x_index]
        self.app.network_frame.input_frame.set_current_input(x)
        self.app.network_frame.update_network_frame()

    def reset_network(self):
        self.app.network.init_network()
        self.app.network_frame.update_network_frame()

    def clear_canvas(self):
        x = np.zeros([self.params.Shapes.image_size, self.params.Shapes.image_size], int)
        self.app.network_frame.input_frame.set_current_input(x)
        self.app.network_frame.update_network_frame()

