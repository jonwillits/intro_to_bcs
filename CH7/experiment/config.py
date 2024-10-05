class Config:
    # general window properties
    window_height = 600
    window_width = 900

    # properties of the instructions
    instructions_bg_color = "white"
    instructions_font_color = "black"
    instructions_font_size = 16
    instructions_font = "helvetica"
    instruction_delay = 1000  # amount of time that timed instructions are on the screen

    # properties of the text and image stimuli
    stimulus_bg_color = "white"
    stimulus_font_color = "black"
    stimulus_font_size = 32
    stimulus_font = "helvetica"
    image_stimulus_height = 400
    image_stimulus_width = 400
    inter_trial_interval = 1000  # amount of time between trials, in ms
    stimulus_presentation_time = 1000  # amount of time each word or image is on the screen

    # properties of the familiarization phase
    num_familiarization_trials = 4
    familiarization_key_list = None  # which keys end trial, if None, will end after stimulus presentation time

    # properties of the test phase
    num_test_trials = 4
    test_from_fam_proportion = 0.5  # percentage of test trials that were in the familiarization condition
    test_key_list = ["j", "k"]
    test_delay = 1000  # amount of time between familiarization and test phases

    # properties defining differences between text and image conditions
    condition = 2  # sets whether we will use words (0) or pictures (1) in the experiment
    instruction_file_path_list = ["stimuli/word_instructions.txt", "stimuli/word_instructions.txt", "stimuli/image_instructions.txt"]
    stimulus_type_list = ["words", "nonwords", "images"]