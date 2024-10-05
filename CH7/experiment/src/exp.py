import csv
import random
import datetime
import os


class Exp:

    def __init__(self, the_app, params):
        self.the_app = the_app  # an instance of the Gui class, which we will use to present info to the screen
        self.params = params  # the experiment parameter data class
        self.stimulus_type_list = self.params.stimulus_type_list
        self.stimulus_type = None
        self.block_number = None

        self.participant_id = None  # a unique number for each participant that we will create

        self.instruction_list = None  # a list of strings containing the data in the instruction file
        self.full_stimulus_list = None  # a list of all the possible words/images for the experiment
        self.familiarization_list = None  # the list of words in this participant's familiarization phase
        self.test_list = None  # the list of words in this participant's test list

        self.data_list = []  # a list that will keep track of the data for each trial in the experiment

        self.create_participant_id()  # a method that will generate an id number of the participant
        random.shuffle(self.stimulus_type_list)

        for i, stimulus_type in enumerate(self.stimulus_type_list):
            self.block_number = i + 1
            self.stimulus_type = self.stimulus_type_list[i]
            self.create_instruction_lists()  # a method that will load the data from the instructions text file
            self.create_stimuli_lists()  # a method that will create the list of possible stimuli from the image folder
            self.run_experiment()  # a method that will run the actual experiment
        self.the_app.show_instructions(self.instruction_list[5], True)
        self.save_data()

        self.the_app.root.destroy()

    def create_participant_id(self):
        current_datetime = datetime.datetime.now()  # gets the current date at time as a datetime object
        formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S%f")  # converts the datetime object to a string
        random_number = random.randint(100000, 999999)  # choose a random 6-digit number
        self.participant_id = f"{formatted_datetime}_{random_number}"  # save combination as the participant id

    def create_instruction_lists(self):
        self.instruction_list = []  # create the empty list
        current_condition = self.params.condition # get the current condition (word or image) from the config file
        instruction_filename = self.params.instruction_file_path_list[current_condition]  # get file path from config file

        with open(instruction_filename, 'r') as file:  # open the instruction file in read mode
            for line in file:  # for each line in the file
                line = line.strip('\n')  # strip off the newlines from each line in the file
                line = line.replace(".", ".\n")  # replace every period in the current line with a period followed by \n
                self.instruction_list.append(line) # add the string to the instruction list

    def load_nonword_list(self):
        nonword_file = 'stimuli/nonwords.txt'
        nonword_list = []

        # Open the file with the correct encoding
        with open(nonword_file, 'r', encoding='utf-16') as file:
            for line in file:
                nonword_list.append(line.strip())  # strip removes any surrounding whitespace including newlines

        return nonword_list

    def create_full_stimulus_list(self):
        if self.stimulus_type == "nonwords":
            self.full_stimulus_list = self.load_nonword_list()
        elif self.stimulus_type == "words" or self.stimulus_type == "images":
            directory_list = os.listdir('stimuli/images/')  # get a list of all the files in the images directory
            self.full_stimulus_list = []  # create the empy stimulus list
            for thing in directory_list:  # loop through the list of files in the images directory
                if not thing.startswith("."):  # if the current item is not a hidden file (hidden files start with ".")
                    self.full_stimulus_list.append(thing[:-4])  # append its name to the stimulus list, minus the file ending

            # if this experiment uses images, call the Gui's preload images method, passing it the list of stimulus names
            if self.stimulus_type == "images":
                self.the_app.preload_images(self.full_stimulus_list)
        else:
            raise Exception(f"Invalid stimulus type {self.stimulus_type}")

    def create_stimuli_lists(self):
        self.create_full_stimulus_list()  # call a function to create the full stimulus list
        self.create_familiarization_list() # call a function to create the full stimulus list
        self.create_test_list() # call a function to create the full stimulus list
        random.shuffle(self.familiarization_list) # randomize the order of the stimuli
        random.shuffle(self.test_list) # randomize the order of the stimuli

    def create_familiarization_list(self):
        random.shuffle(self.full_stimulus_list)  # randomize the stimulus list

        # select teh first num_familiarization_trials items from the randomized list
        self.familiarization_list = self.full_stimulus_list[:self.params.num_familiarization_trials]

    def create_test_list(self):
        # determine how many test trials should come from the familiarization list
        num_old_test_trials = self.params.num_test_trials // 2

        # get half of our test items from the familiarization list.
        # this is why we have to remember to shuffle the order of our familiarization and test lists in the
        # create_stimuli_lists() method, since we don't want the participant to experience the first half of the test
        # list as old items, or the first half of the familiarization list as test items
        self.test_list = self.familiarization_list[:num_old_test_trials]

        # to get our new items, we need to create an index corresponding to the num of fam trials, where we left off
        # when we took items from the full stimulus list when we generated the familiarization list
        start = self.params.num_familiarization_trials

        # the position in the full stimulus list where we will stop drawing new stimuli for the test list
        stop = start + self.params.num_test_trials // 2

        # get the rest of our test list using those two indexes
        self.test_list += self.full_stimulus_list[start:stop]

    def run_experiment(self):
        self.the_app.show_instructions(self.instruction_list[0], True)
        self.the_app.show_instructions(self.instruction_list[1], False)
        self.the_app.show_instructions(self.instruction_list[2], False)
        self.the_app.show_instructions(self.instruction_list[3], False)
        self.present_stimulus_list(self.familiarization_list, self.params.familiarization_key_list, False)

        self.the_app.show_instructions(self.instruction_list[4], True)
        self.the_app.show_instructions(self.instruction_list[1], False)
        self.the_app.show_instructions(self.instruction_list[2], False)
        self.the_app.show_instructions(self.instruction_list[3], False)
        self.present_stimulus_list(self.test_list, self.params.test_key_list, True)

    def present_stimulus_list(self, stimulus_list, key_list, record_data):
        for i, stimulus_name in enumerate(stimulus_list):
            key_pressed, rt = self.the_app.show_stimulus(stimulus_name, key_list, self.stimulus_type)
            if record_data:
                trial_data = [self.stimulus_type,
                              self.block_number,
                              i+1,
                              stimulus_name,
                              key_pressed,
                              rt]
                self.data_list.append(trial_data)

    def save_data(self):
        final_data_list = []  # an empty list where we will put the combined data we aleady had plus the new data

        # insert a new list into our data_list, a list of strings specified what data is stored in each list element
        final_data_list.append(["participant_id",
                                "stimulus_type",
                                "block_number",
                                "trial_number",
                                "stimulus",
                                "condition",
                                "old_trial_number",
                                "response",
                                "correct",
                                "rt"])

        # now we need to go through each trial, and create a list with those 8 items listed above
        for i, trial_data in enumerate(self.data_list):  # for each trial in self.data_list

            stimulus_type = trial_data[0]
            block_number = trial_data[1]
            trial_number = trial_data[2]
            stimulus = trial_data[3]
            rt =f"{trial_data[5]:0.3f}"

            if trial_data[0] in self.familiarization_list:
                condition = 1
                old_trial_number = self.familiarization_list.index(trial_data[0]) + 1
            else:
                condition = 0
                old_trial_number = 0

            if trial_data[4] == "j":
                response = 1
            else:
                response = 0

            # add whether the key that was pressed was the correct key
            if condition == response:
                correct = 1
            else:
                correct = 0

            final_trial_data = [self.participant_id,
                                stimulus_type,
                                block_number,
                                trial_number,
                                stimulus,
                                condition,
                                old_trial_number,
                                response,
                                correct,
                                rt]  # create a new empty list for this trial

            # add the data for the current trial to the full final data list
            final_data_list.append(final_trial_data)

        # create a file with the participant's id number as the file_name, ending with .csv
        filename = f'data/{self.participant_id}.csv'

        # use the csv module to write the full list of lists to the file
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(final_data_list)
