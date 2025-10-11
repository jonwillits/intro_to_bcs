import tkinter as tk
import tkinter.messagebox as messagebox


class OptionsFrame:

    def __init__(self, display):

        self.display = display
        self.options_frame = None

        self.option_frame_dimensions = (150, self.display.window_dimensions[1])
        self.option_start_y = 50
        self.button_height = None
        self.button_width = 10
        self.button_padding = 5
        self.button_spacing = 10
        self.button_list = None

        self.entry_label_x_position = 10
        self.entry_frame_list = None
        self.entry_spacing = 20
        self.entry_start_y = 50
        self.entry_xpadding = 10

        self.create_options_frame()

    def create_options_frame(self):

        self.options_frame = tk.Frame(self.display.root, width=self.option_frame_dimensions[0], bg="slategrey")
        self.options_frame.pack(side="left", fill="y")
        self.display.root.update()

        self.button_list = []
        button_info_list = [("Reset Experiment", 1, "clicked_reset_experiment"),
                            ("Run Experiment", 2, "clicked_run_experiment"),
                            ("Quit", 3, "clicked_quit")]

        for button_info in button_info_list:
            self.button_list.append((self.create_button(button_info), button_info[1]))

        self.option_entry_label_string_list = ["Group1 Mean", "Group1 StDev",
                                               "Group2 Mean", "Group2 StDev",
                                               "Sample Size"]

        self.entry_frame_list = []
        for entry_label_string in self.option_entry_label_string_list:
            self.entry_frame_list.append(self.create_entry_frame(entry_label_string))

        self.options_frame.bind("<Configure>", self.resize)
        self.display.root.update()
        self.display.root.update_idletasks()
        self.resize()

    def create_entry_frame(self, label_string):
        entry_frame = tk.Frame(self.options_frame, bg="slategrey")
        entry_frame.place(x=0, y=0)

        entry = tk.Entry(entry_frame,
                         width=5,
                         bg="white",
                         fg="black",
                         borderwidth=1,
                         highlightthickness=1)  # Create the Entry widget
        default_value = self.display.the_experiment.parameter_dict[label_string]
        entry.pack(side="right")
        entry.insert(0, str(default_value))  # Insert the default value into the Entry widget

        label = tk.Label(entry_frame, text=label_string, bg="slategrey", font=("Helvetica", 11))
        label.pack(side="right")

        return entry_frame

    def create_button(self, button_info):
        command_function = getattr(self, button_info[2])
        button = tk.Button(self.options_frame,
                           text=button_info[0],
                           fg="black",
                           bg="lightgrey",
                           font=("Helvetica", 12),
                           command=command_function,  # will this work, with the function passed in as a string?
                           width=self.button_width,
                           padx=self.button_padding,
                           pady=self.button_padding,
                           borderwidth=1,
                           highlightthickness=1,
                           relief="flat")

        button.place(x=0, y=0)
        return button

    def resize(self, event=None):
        """Reposition buttons based on the current height of the options frame."""
        total_button_height = self.position_buttons()
        self.position_entry_frames(total_button_height)

    def position_buttons(self):
        total_button_height = 0
        button_height = 0
        for button, position in self.button_list:
            button_width = button.winfo_reqwidth()
            button_height = button.winfo_reqheight()
            total_button_height += button_height

            x_position = (self.options_frame.winfo_width() - button_width) // 2  # Center the button horizontally

            if position == 1:
                y_position = self.option_start_y
            elif position == 2:
                y_position = self.option_start_y + button_height + self.button_spacing
            elif position == 3:
                y_position = self.options_frame.winfo_height() - button_height - 10
            else:
                raise Exception("ERROR: Unrecognized button position")

            button.place_configure(x=x_position, y=y_position)

        return total_button_height - button_height

    def position_entry_frames(self, total_button_height):
        y_position = self.option_start_y + total_button_height + (
                    len(self.button_list) - 2) * self.button_spacing + self.entry_start_y
        entry_height = 0

        for i, entry_frame in enumerate(self.entry_frame_list):
            # Get the width of the parent frame and the entry frame
            parent_width = self.options_frame.winfo_width()
            entry_frame_width = entry_frame.winfo_width()

            # Calculate the x position to right-align the entry frame
            x_position = parent_width - entry_frame_width - self.entry_xpadding  # 10 pixels padding from the right edge

            # Position the entry frame
            entry_frame.place_configure(x=x_position, y=y_position + entry_height)

            # Update the cumulative height for the next entry frame
            entry_height += entry_frame.winfo_height() + self.entry_spacing

    def clicked_run_experiment(self):
        pass

    def clicked_quit(self):
        self.display.root.destroy()

    def clicked_reset_experiment(self):
        for entry_frame, label_string in zip(self.entry_frame_list, self.option_entry_label_string_list):
            entry_widget = entry_frame.winfo_children()[0]  # Assuming Entry is the first child widget in entry_frame
            entry_value = entry_widget.get()

            invalid_entry = False
            error_message = ""

            if self.display.the_experiment.parameter_dict[label_string].is_integer():
                was_int = True
            else:
                was_int = False

            # Validate that the entry is a number
            try:
                entry_value = float(entry_value)
            except ValueError:
                invalid_entry = True
                error_message = "Please enter numeric values in all fields."

            # Additional validation for "Sample Size" to ensure it's a positive integer
            if not invalid_entry and label_string == 'Sample Size':
                if not entry_value.is_integer() or entry_value <= 0:
                    invalid_entry = True
                    error_message = "Please enter a positive integer for sample size."

            # If there is an invalid entry, reset the field and show an error message
            if invalid_entry:
                previous_value = self.display.the_experiment.parameter_dict[label_string]
                if was_int:
                    previous_value = int(previous_value)
                entry_widget.delete(0, tk.END)
                entry_widget.insert(0, str(previous_value))
                messagebox.showerror("Invalid Input", error_message)
            else:
                if label_string == 'Sample Size':
                    entry_value = int(entry_value)
                self.display.the_experiment.parameter_dict[label_string] = entry_value

        for key, value in self.display.the_experiment.parameter_dict.items():
            print(key, value)

