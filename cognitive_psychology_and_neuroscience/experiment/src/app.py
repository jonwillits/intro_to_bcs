import tkinter as tk
import time
from PIL import Image, ImageTk


class App:

    def __init__(self, params):
        self.params = params
        self.root = None  # the variable where we will store the main window
        self.stimulus_label = None  #  a tkinter label widget that we will use to present text or images
        self.instructions_label = None  #  a tkinter label widget that we will use to present instructions
        self.key_pressed = None  # variable we will use to keep track of which key has been pressed
        self.image_dict = None  # a dictionary of image names pointing to tk image objects


        self.create_window()
        self.create_labels()

    def create_window(self):
        self.root = tk.Tk()  # create the tk window object and save it in self.root
        self.root.geometry("{}x{}".format(self.params.window_width, self.params.window_height))  # set the window size
        self.root.title("Experiment")  # set the window title
        self.root.configure(bg="white")  # set the window background color
        self.root.resizable(False, False)  # set the window so that it is not resizable

    def create_labels(self):
        self.instructions_label = tk.Label(self.root, anchor='center',
                                           height=self.params.window_height,
                                           width=self.params.window_width,
                                           bg=self.params.instructions_bg_color,
                                           fg=self.params.instructions_font_color,
                                           font="{} {}".format(self.params.instructions_font,
                                                               self.params.instructions_font_size))

        self.stimulus_label = tk.Label(self.root, anchor='center',
                                       height=self.params.window_height,
                                       width=self.params.window_width,
                                       bg=self.params.stimulus_bg_color,
                                       fg=self.params.stimulus_font_color,
                                       font="{} {}".format(self.params.stimulus_font,
                                                           self.params.stimulus_font_size))

    def preload_images(self, image_name_list):
        self.image_dict = {}  # create an empty dictionary to store the images
        for image_name in image_name_list:  # for each image name in the image name list
            image = Image.open("stimuli/images/" + image_name + ".jpg") # create a PIL image object for that image name
            photo_image = ImageTk.PhotoImage(image)  # convert the PIL image object into a TK image object
            self.image_dict[image_name] = photo_image  # save the image in the dictionary with its name as a the key

    def show_instructions(self, instructions, end_on_key_press=False, extra_delay=None):
        self.instructions_label.configure(
            text=instructions)  # set the text property of the label to the instruction string
        self.instructions_label.pack()  # make the label appear in the window
        self.instructions_label.pack_propagate(False)  # prevent the label from changing size to fit the text
        self.root.update()  # force the window to update its graphics and reflect the changes that were made

        if end_on_key_press:  # if we want to end the instructions after a key has been pressed
            self.key_pressed = None  # set our variable reflecting whether a key has been pressed to False

            # create a tkinter event that activates whenever a key has been pressed
            # when a key has been pressed it calls the specified function check_for_valid_key_press()
            # we pass that function a list of key names that we are considering to be "valid" keys to press to end the
            #    instructions. When a valid key is pressed, that function will set self.key pressed to that key
            self.root.bind('<Key>', lambda event: self.check_for_valid_key_press(event, ["space"]))

            # create a loop that runs while self.key_pressed is False
            # since we set key_pressed to None, which evaluates to False, the loop will run until key_pressed is set
            # to something other than "None" by the self.check_for_valid_key_press() method
            while not self.key_pressed:
                self.root.update()

        else:  # if we do not want to end on a key press
            self.root.after(
                self.params.instruction_delay)  # sit and do nothing for the amount of time specified in the config file

        # sit and do nothing for an additional amount of time, if specified by extra_delay
        if extra_delay is not None:
            self.root.after(extra_delay)

        self.instructions_label.pack_forget()  # remove the instruction_text_label from the window

    def check_for_valid_key_press(self, event, valid_keys):
        if event.keysym in valid_keys:  # check to see if the key that was pressed is one of the valid keys

            # gets rid of the event checking for key presses, meaning we only will get an event after the first key press
            self.root.unbind('<Key>')

            # makes sure the main window is the active window in the program after the key press
            # this is just there as a precaution in case the key press did something unexpected
            self.root.focus_set()

            self.key_pressed = event.keysym  # set our variable keeping track of what key was pressed to the current value

    def show_stimulus(self, stimulus_name, key_list, stimulus_type):

        if stimulus_type == "words" or stimulus_type == "nonwords":  # if we are in the word condition
            self.stimulus_label.configure(text=stimulus_name)  # change the text to the current stimulus name
        elif stimulus_type == "images":  # elif we are in the image condition
            stimulus_image = self.image_dict[stimulus_name]  # retrieve the image from the image dict
            # set the label to the current image. This requires both lines below.
            self.stimulus_label.configure(image=stimulus_image)
            self.stimulus_label.image = stimulus_image

        self.stimulus_label.pack()  # show the stimulus label in the window
        self.stimulus_label.pack_propagate(False)  # prevent the label from changing size to fit the image or text
        self.root.update()  # force the window to update and show whatever changes we have made
        time1 = time.time()  # get the current system time, reflecting the exact moment the stimulus went on screen

        if key_list is not None:
            self.key_pressed = None  # set key_pressed back to None

            # just like before, create a tkinter event that activates whenever a key has been pressed
            # when a key has been pressed it calls the specified function check_for_valid_key_press()
            # we pass that function a list of key names that we are considering to be "valid" keys to press to end the
            # stimulus presentation. When a valid key is pressed, that function will set self.key pressed to that key
            self.root.bind('<Key>', lambda event: self.check_for_valid_key_press(event, key_list))

            # create a loop that runs while self.key_pressed is False
            # since we set key_pressed to None, which evaluates to False, the loop will run until key_pressed is set
            # to something other than "None" by the self.check_for_valid_key_press() method
            while not self.key_pressed:  # loop until self.key_pressed is not None
                self.root.update()

        else:  # if key_list is set to None, then sit and do nothing for the specified amount of time
            self.root.after(self.params.stimulus_presentation_time)

        time2 = time.time()  # get the exact system time
        # compute the time different between when the stimulus was presented and the end of the stimulus, which will
        # correspond to how long it took the participant to respond in the trials where a key must be pressed
        took = time2 - time1

        self.stimulus_label.pack_forget()  # remove the stimulus from the screen

        # do nothing for the amount of time we want to delay between stimuli, specified in the Config file
        self.root.after(self.params.inter_trial_interval)

        return self.key_pressed, took  # return the key that was pressed and how it took