import tkinter as tk

class InterfaceFrame:

    def __init__(self, app):
        self.app = app
        self.frame = None
        self.dataset_label = None
        self.num_epochs_label = None
        self.epoch_entry = None
        self.train_button = None
        self.reset_button = None
        self.quit_button = None
        self.interface_object_list = None
        self.dataset_list = None
        self.dataset_option_menu = None
        self.selected_dataset = None

        self.create_interface_frame()

    def create_interface_frame(self):
        self.interface_object_list = []

        self.frame = tk.Frame(self.app.root,
                              height=self.app.interface_height,  # Fixed height
                              bg="#222222")

        self.frame.pack(fill=tk.X, side=tk.TOP)

        self.dataset_label = tk.Label(self.frame, text="Dataset", bg="#222222", fg="white")
        self.dataset_label.pack(side=tk.LEFT, padx=5)

        # Create and pack the drop-down menu for datasets
        self.dataset_list = ["AND", "OR", "XOR", "x1", "x2", "Random"]  # Example dataset list
        self.selected_dataset = tk.StringVar(self.frame)
        self.selected_dataset.set(self.dataset_list[0])  # Default to the first option

        self.dataset_option_menu = tk.OptionMenu(self.frame, self.selected_dataset, *self.dataset_list,
                                                 command=self.app.change_dataset)
        self.dataset_option_menu.config(width=10, bg="white", fg="black")
        self.dataset_option_menu.pack(side=tk.LEFT, padx=5)

        # create and pack the num epochs label
        self.num_epochs_label = tk.Label(self.frame, text="Training Epochs", bg="#222222", fg="white")
        self.num_epochs_label.pack(side=tk.LEFT)

        # Entry widget for user input
        self.epoch_entry = tk.Entry(self.frame, width=5, bg="white", fg="black")
        self.epoch_entry.pack(side=tk.LEFT, padx=10)
        self.epoch_entry.insert(0, "1")  # Default value

        # Train button
        self.train_button = tk.Button(self.frame, text="Train", command=self.app.train_from_entry, width=10)
        self.train_button.pack(side=tk.LEFT, padx=2)
        self.interface_object_list.append(self.train_button)

        # Reset button
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.app.reset, width=10)
        self.reset_button.pack(side=tk.LEFT, padx=2)
        self.interface_object_list.append(self.reset_button)

        # Quit button
        self.quit_button = tk.Button(self.frame, text="Quit", command=self.app.quit, width=10)
        self.quit_button.pack(side=tk.RIGHT, padx=5)