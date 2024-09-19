import tkinter as tk
import math
import numpy as np
from . import activation_frame

class App:
    def __init__(self, params, network, dataset):
        self.network = network
        self.dataset = dataset

        self.root = None
        self.main_window_dimensions = params.dimensions

        self.interface_frame = None
        self.dataset_label = None
        self.num_epochs_label = None
        self.epoch_entry = None
        self.train_button = None
        self.reset_button = None
        self.quit_button = None
        self.interface_height = 150
        self.button_list = None
        self.dataset_list = None
        self.dataset_option_menu = None
        self.selected_dataset = None

        self.main_frame = None
        self.main_frame_dimensions = (self.main_window_dimensions[0],
                                      self.main_window_dimensions[1]-self.interface_height)
        self.item_frame = None
        self.network_frame = None
        self.activation_frame = None
        self.classification_frame = None
        self.item_canvas = None
        self.network_canvas = None
        self.activation_canvas = None
        self.classification_canvas = None
        self.performance_frame = None
        self.performance_canvas = None

        self.current_item_index = 0
        self.total_epochs = 0
        #
        # self.node_radius = 30
        # self.thickness = 3
        # self.y0_pos = (350, 200)
        # self.x0_pos = (100, 350)
        # self.x1_pos = (250, 500)
        # self.x2_pos = (450, 500)

        self.create_main_window()
        self.create_interface_frame()
        self.init_main_frame()
        self.draw_main_frame()
        # self.weight_window = None

    def create_main_window(self):
        self.root = tk.Tk()
        self.root.title("Neural Network")
        self.root.geometry(f'{self.main_window_dimensions[0]}x{self.main_window_dimensions[1]}')
        self.root.configure(background='blue')
        self.root.update_idletasks()  # Ensure correct initialization of sizes

    def create_interface_frame(self):
        # Set the frame to have a fixed height of 50 pixels and fill the width
        self.interface_frame = tk.Frame(self.root,
                                        height=50,  # Fixed height
                                        bg="#222222")

        self.interface_frame.pack(fill=tk.X, side=tk.TOP)

        self.dataset_label = tk.Label(self.interface_frame, text="Dataset", bg="#222222", fg="white")
        self.dataset_label.pack(side=tk.LEFT, padx=5)

        # Create and pack the drop-down menu for datasets
        self.dataset_list = ["AND", "OR", "XOR", "x1", "x2", "Random"]  # Example dataset list
        self.selected_dataset = tk.StringVar(self.interface_frame)
        self.selected_dataset.set(self.dataset_list[0])  # Default to the first option

        self.dataset_option_menu = tk.OptionMenu(self.interface_frame, self.selected_dataset, *self.dataset_list,
                                                 command=self.change_dataset)
        self.dataset_option_menu.config(width=10, bg="white", fg="black")
        self.dataset_option_menu.pack(side=tk.LEFT, padx=5)

        # create and pack the num epochs label
        self.num_epochs_label = tk.Label(self.interface_frame, text="Training Epochs", bg="#222222", fg="white")
        self.num_epochs_label.pack(side=tk.LEFT)

        # Entry widget for user input
        self.epoch_entry = tk.Entry(self.interface_frame, width=5, bg="white", fg="black")
        self.epoch_entry.pack(side=tk.LEFT, padx=10)
        self.epoch_entry.insert(0, "1")  # Default value

        # Train button
        self.train_button = tk.Button(self.interface_frame, text="Train", command=self.train_from_entry, width=10)
        self.train_button.pack(side=tk.LEFT, padx=2)

        # Reset button
        self.reset_button = tk.Button(self.interface_frame, text="Reset", command=self.reset, width=10)
        self.reset_button.pack(side=tk.LEFT, padx=2)

        # Quit button
        self.quit_button = tk.Button(self.interface_frame, text="Quit", command=self.quit, width=10)
        self.quit_button.pack(side=tk.RIGHT, padx=5)

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

    def init_main_frame(self):
        self.main_frame = tk.Frame(self.root, bg="grey")
        self.main_frame.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        self.activation_frame = activation_frame.ActivationFrame(self)

        self.item_frame = tk.Frame(self.main_frame, bg="red", height=100, width=100)
        # self.item_frame.place(x=self.main_frame_dimensions[0]//2, y=0)
        self.item_canvas = tk.Canvas(self.item_frame, bg="#BBBBBB", height=100, width=100, borderwidth=0, highlightthickness=0)
        # self.item_canvas.pack(fill=tk.BOTH, expand=True)

        self.network_frame = tk.Frame(self.main_frame, bg="green", height=100, width=100)
        # self.network_frame.place(x=0, y=self.main_frame_dimensions[1]//2)
        self.network_canvas = tk.Canvas(self.network_frame, bg="#BBBBBB", height=100, width=100, borderwidth=0, highlightthickness=0)
        # self.network_canvas.pack(fill=tk.BOTH, expand=True)

        self.classification_frame = tk.Frame(self.main_frame, bg="yellow", height=100, width=100)
        # self.classification_frame.place(x=2*self.main_frame_dimensions[0]//3, y=self.main_frame_dimensions[1]//2)
        self.classification_canvas = tk.Canvas(self.classification_frame, bg="#BBBBBB", height=100, width=100, borderwidth=0, highlightthickness=0)
        # self.classification_canvas.pack(fill=tk.BOTH, expand=True)

        self.performance_frame = tk.Frame(self.main_frame, bg="purple", height=100, width=100)
        # self.performance_frame.place(x=1*self.main_frame_dimensions[0]//3, y=self.main_frame_dimensions[1]//2)
        self.performance_canvas = tk.Canvas(self.performance_frame, bg="#BBBBBB", height=100, width=100, borderwidth=0, highlightthickness=0)
        # self.performance_canvas.pack(fill=tk.BOTH, expand=True)

    def wait_and_do_nothing(self):
        for button in self.button_list:
            button.config(state=tk.DISABLED)
        self.root.after(500)
        for button in self.button_list:
            button.config(state=tk.NORMAL)

    def train_from_entry(self):
        # Get the value from the Entry box
        num_epochs_str = self.epoch_entry.get()

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
        self.draw_network_frame()
        self.activation_frame.draw_frame()
        self.draw_classification_frame()
        self.draw_performance_frame()
        self.draw_item_frame()
        self.root.update()

    def draw_network_frame(self):
        self.network_canvas.delete("all")

    def draw_classification_frame(self):
        self.classification_canvas.delete("all")

    def draw_performance_frame(self):
        self.performance_canvas.delete("all")

    def draw_item_frame(self):
        self.item_canvas.delete("all")
        start_x = 50
        start_y = 10
        button_height = 32
        button_width = 60

        self.item_canvas.create_text(start_x, start_y, text="Dataset:", font="Arial 20 bold", fill="#000000")
        # self.network_canvas.create_rectangle(start_x+50,
        #                                      start_y-10,
        #                                      start_x+button_width+50,
        #                                      button_height+button_height,
        #                                      fill="#AAAAAA", activefill="black", tags='dataset_button')
        # self.network_canvas.create_text(start_x + 80, start_y+2, text=self.dataset,
        #                                 font="Arial 16 bold",
        #                                 fill="#444444", tags='dataset_button')
        #
        # header = "x1     x2        y    prediction"
        # self.network_canvas.create_text(start_x + 50, start_y+35, text=header, font="Arial 16 bold", fill="black")
        # self.network_canvas.create_line(start_x-70, start_y+50, start_x+145, start_y+50,
        #                                 width=self.thickness, fill="black")
        # self.network_canvas.create_line(start_x+30, start_y+30, start_x+30, start_y+170,
        #                                 width=self.thickness, fill="black")
        # for i in range(self.network.dataset.n):
        #     x = self.network.dataset.items[self.dataset][0][i]
        #     y = self.network.dataset.items[self.dataset][1][i][0]
        #     y_predict = self.network.forward(x, self.params['activation_function'])
        #     items = "{:0.0f}       {:0.0f}         {:0.0f}     {:0.3f}".format(x[0], x[1], y, y_predict[0,0])
        #     tag = "item" + str(i)
        #     self.network_canvas.create_text(start_x+40, start_y+35+(i+1)*30, text=items, font="Arial 16 bold", fill="black", tags=tag)
        #
        #

    # def draw_boundary(self):
    #
    #     self.network_canvas.create_text(665, 350, text="Decision Boundary", font="Arial 20 bold", fill="#000000")
    #     precision = 0.01
    #     y1 = -100
    #     n = 100
    #     y1_predict = 0
    #     while abs(y1_predict - 0.50) > precision:
    #         y1_predict = self.network.forward([0, y1], self.params['activation_function'])[0, 0]
    #         y1 += 1/n
    #         if y1 > 100:
    #             break
    #     y2 = -100
    #     n = 100
    #     y2_predict = 0
    #     while abs(y2_predict - 0.50) > precision:
    #         y2_predict = self.network.forward([1, y2], self.params['activation_function'])[0, 0]
    #         y2 += 1/n
    #         if y2 > 100:
    #             break
    #     m = (y2-y1)
    #     b = y1
    #     equation = "y = {:0.3f}x + {:0.3f}".format(m, b)
    #     self.network_canvas.create_text(665, 380, text=equation, font="Arial 14 bold", fill="#000000")
    #     x_is_0 = 620
    #     y_is_0 = 540
    #     scale = 100
    #
    #     coord_list = []
    #     x = -1
    #     for i in range(300):
    #         y = m * x + b
    #         if -1 <= y <= 2:
    #             coord_list.append((x, y))
    #         x += 0.01
    #
    #     self.network_canvas.create_line(x_is_0, y_is_0, x_is_0+scale, y_is_0, width=self.thickness)
    #     self.network_canvas.create_line(x_is_0, y_is_0, x_is_0, y_is_0-scale, width=self.thickness)
    #     self.network_canvas.create_line(x_is_0, y_is_0-scale, x_is_0 + scale, y_is_0-scale, width=self.thickness)
    #     self.network_canvas.create_line(x_is_0+scale, y_is_0, x_is_0 + scale, y_is_0-scale, width=self.thickness)
    #
    #     if len(coord_list) > 1:
    #         self.network_canvas.create_line(x_is_0+coord_list[0][0]*scale,
    #                                         y_is_0-coord_list[0][1]*scale,
    #                                         x_is_0 + coord_list[-1][0] * scale,
    #                                         y_is_0 - coord_list[-1][1] * scale,
    #                                         width=self.thickness, fill='yellow')
    #
    #     x_is_0 = 620
    #     y_is_0 = 440
    #     scale = 100
    #     node_radius = 4
    #     for i in range(self.network.dataset.n):
    #         x1 = self.network.dataset.items[self.dataset][0][i][0]
    #         x2 = self.network.dataset.items[self.dataset][0][i][1]
    #         y = self.network.dataset.items[self.dataset][1][i][0]
    #         if y == 1:
    #             color = 'green'
    #         else:
    #             color = 'red'
    #         self.network_canvas.create_oval(x_is_0 + scale * x1 - node_radius,
    #                                         y_is_0 + scale * abs(x2 - 1) - node_radius,
    #                                         x_is_0 + scale * x1 + node_radius,
    #                                         y_is_0 + scale * abs(x2 - 1) + node_radius,
    #                                         fill=color)
    #         label = "({},{})".format(x1, x2)
    #         self.network_canvas.create_text(590 + 150 * x1, 420 + 140 * abs(x2 - 1), text=label, font="Arial 14 bold",
    #                                         fill="#000000")


    # def network_click(self, event):
    #     x, y = event.x, event.y
    #     ids = self.network_canvas.find_overlapping(x-5, y-5, x+5, y+5)
    #     if len(ids) > 0:
    #         the_tag = self.network_canvas.itemcget(ids[0], "tags").split()[0]
    #         if the_tag in ['item0', 'item1', 'item2', 'item3']:
    #             self.current_item_index = int(the_tag[-1])
    #             self.current_x = self.network.dataset.items[self.dataset][0][self.current_item_index]
    #             self.current_y = self.network.dataset.items[self.dataset][1][self.current_item_index]
    #             self.draw_network_frame()
    #         elif the_tag == 'dataset_button':
    #             if self.dataset == 'AND':
    #                 self.dataset = 'OR'
    #             elif self.dataset == 'OR':
    #                 self.dataset = 'XOR'
    #             elif self.dataset == 'XOR':
    #                 self.dataset = 'x1'
    #             elif self.dataset == 'x1':
    #                 self.dataset = 'x2'
    #             elif self.dataset == 'x2':
    #                 self.dataset = 'AND'
    #             self.draw_network_frame()
    #         elif the_tag in ['b0', 'b1', 'b2']:
    #             tk.Message(text='Change Weight?')
    #             d = GetWeightDialog(self, the_tag)
    #             self.root.wait_window(d.top)
    #             self.draw_network_frame()

    @staticmethod
    def get_hex_color(value):
        if value > 1:
            value = 1
        if value < -1:
            value = -1

        abs_value = 1 - abs(value)
        scaled_value = int(round(255 * abs_value, 0))
        hex_value = hex(scaled_value)[2:]

        if len(hex_value) == 1:
            hex_value = "0" + hex_value

        if value > 0:
            return '#{}ff{}'.format(hex_value, hex_value)
        elif value < 0:
            return '#ff{}{}'.format(hex_value, hex_value)
        else:
            return "#ffffff"


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
