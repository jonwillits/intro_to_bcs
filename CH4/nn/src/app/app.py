import tkinter as tk
from . import dataset_frame, activation_frame, classification_frame, network_frame, performance_frame, interface_frame

class App:
    def __init__(self, params, network, dataset):
        self.network = network
        self.dataset = dataset

        self.root = None
        self.main_window_dimensions = params.dimensions

        self.interface_frame = None
        self.interface_height = 50

        self.main_frame = None
        self.main_frame_dimensions = (self.main_window_dimensions[0],
                                      self.main_window_dimensions[1]-self.interface_height)
        self.dataset_frame = None
        self.network_frame = None
        self.activation_frame = None
        self.classification_frame = None
        self.performance_frame = None

        self.current_item_index = 0
        self.total_epochs = 0

        self.create_main_window()
        self.create_interface_frame()
        self.create_main_frame()
        self.draw_main_frame()

    def create_main_window(self):
        self.root = tk.Tk()
        self.root.title("Neural Network")
        self.root.geometry(f'{self.main_window_dimensions[0]}x{self.main_window_dimensions[1]}')
        self.root.configure(background='blue')
        self.root.update_idletasks()  # Ensure correct initialization of sizes

    def create_interface_frame(self):
        # Set the frame to have a fixed height of 50 pixels and fill the width
        self.interface_frame = interface_frame.InterfaceFrame(self)

    def change_dataset(self, selected_option):
        # Placeholder function that will receive the selected option
        print(f"Selected dataset: {selected_option}")
        if selected_option == "AND":
            self.dataset.dataset_type = "and"
        elif selected_option == "OR":
            self.dataset.dataset_type = "or"
        elif selected_option == "XOR":
            self.dataset.dataset_type = "xor"
        elif selected_option == "x1":
            self.dataset.dataset_type = "x1"
        elif selected_option == "x2":
            self.dataset.dataset_type = "x2"
        elif selected_option == "Random":
            self.dataset.dataset_type = "random"
        else:
            raise Exception("ERROR: Dataset type not supported")
        self.dataset.generate_y_lists()
        self.draw_main_frame()

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root, bg="#BBBBBB")
        self.main_frame.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        self.dataset_frame = dataset_frame.DatasetFrame(self,
                                                        x=0,
                                                        y=0,
                                                        height=self.main_frame_dimensions[1]//3,
                                                        width=self.main_frame_dimensions[0]//3)

        # self.performance_frame = performance_frame.PerformanceFrame(self,
        #                                                             x=self.main_frame_dimensions[0]//3,
        #                                                             y=0,
        #                                                             height=self.main_frame_dimensions[1]//3,
        #                                                             width=self.main_frame_dimensions[0]//3)

        self.classification_frame = classification_frame.ClassificationFrame(self,
                                                                             x=2*self.main_frame_dimensions[0]//3,
                                                                             y=0,
                                                                             height=self.main_frame_dimensions[1]//3,
                                                                             width=self.main_frame_dimensions[0]//3)

        self.network_frame = network_frame.NetworkFrame(self,
                                                        x=0,
                                                        y=self.main_frame_dimensions[1]//3,
                                                        height=2*self.main_frame_dimensions[1]//3,
                                                        width=2*self.main_frame_dimensions[0]//3)

        self.activation_frame = activation_frame.ActivationFrame(self,
                                                                 x=2*self.main_frame_dimensions[0]//3,
                                                                 y=self.main_frame_dimensions[1]//3,
                                                                 height=2*self.main_frame_dimensions[1]//3,
                                                                 width=self.main_frame_dimensions[0]//3)



    def wait_and_do_nothing(self):
        for button in self.interface_frame.interface_object_list:
            button.config(state=tk.DISABLED)
        self.root.after(100)
        for button in self.interface_frame.interface_object_list:
            button.config(state=tk.NORMAL)

    def train_from_entry(self):
        # Get the value from the Entry box
        num_epochs_str = self.interface_frame.epoch_entry.get()

        # Validate the input and convert to integer
        try:
            num_epochs = int(num_epochs_str)
            if num_epochs > 0:
                self.train(num_epochs)
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def train(self, num_epochs):
        print(f"Training for {num_epochs} epochs")
        for i in range(num_epochs):
            x = self.dataset.x
            y = self.dataset.y
            self.total_epochs += 1
            output_array, rounded_output, agreement, percent_correct, mean_cost = self.network.train(x, y)
            if self.total_epochs % 5 == 0:
                print(self.total_epochs, percent_correct, mean_cost)
            self.draw_main_frame()

    def reset(self):
        self.network.init_network()
        self.draw_main_frame()
        self.root.update()

    def quit(self):
        self.root.quit()

    def draw_main_frame(self):
        self.network_frame.draw_frame()
        self.activation_frame.draw_frame()
        self.classification_frame.draw_frame()
        if self.performance_frame is not None:
            self.performance_frame.draw_frame()
        self.dataset_frame.draw_frame()
        self.root.update()

    def network_click(self, event):
        x, y = event.x, event.y
        ids = self.network_frame.canvas.find_overlapping(x-5, y-5, x+5, y+5)
        if len(ids) > 0:
            the_tag = self.network_frame.canvas.itemcget(ids[0], "tags").split()[0]
            if the_tag in ['item0', 'item1', 'item2', 'item3']:
                self.current_item_index = int(the_tag[-1])
                self.network_frame.draw_frame()
            elif the_tag in ['b0', 'b1', 'b2']:
                tk.Message(text='Change Weight?')
                d = GetWeightDialog(self, the_tag)
                self.root.wait_window(d.top)
                self.network_frame.draw_frame()


############################################################################################################
############################################################################################################
class GetWeightDialog:
    def __init__(self, display, the_tag):
        self.display = display
        top = self.top = tk.Toplevel(display.root)
        self.the_tag = the_tag
        tk.Label(top, text="Value").pack()
        self.e = tk.Entry(top)
        self.e.pack(padx=5)
        b = tk.Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        value = self.e.get()
        if self.the_tag == 'b0':
            self.display.network.y_bias[0, 0] = float(value)
        if self.the_tag == 'b1':
            self.display.network.y_x[0,0] = float(value)
        if self.the_tag == 'b2':
            self.display.network.y_x[0,1] = float(value)
        self.top.destroy()
