import tkinter as tk
from PIL import Image, ImageTk  # Import from Pillow
import tkinter.font as tkfont  # Import font module


class App:
    """
    A class that creates a Tkinter-based GUI for a Rock-Paper-Scissors game.
    The class handles user interactions, displays game results, and optionally shows AI behavior.

    Attributes:
        the_game (object): The game logic, which must have methods such as `play_round()`, `init_game()`, and track
            game state such as `num_rounds`, `score`, and `history_dict_list`.
        show_ai (bool): Whether to display AI behavior and explanation in the GUI.
        root (tk.Tk): The main application window.
        app_dimensions (tuple): The dimensions of the app window.
        main_frame (tk.Frame): The main frame containing the buttons and labels.
        rock_button, paper_button, scissors_button (tk.Button): Buttons for player to choose Rock, Paper, or Scissors.
        round_label, wins_label, losses_label, ties_label (tk.Label): Labels displaying game stats (rounds, wins, losses, ties).
        history_label (tk.Label): Label displaying the last few game results.
        memory_matrix_label (tk.Label): Label displaying AI memory matrix data.

    Methods:
        create_app_window():
            Initializes and configures the main app window, creates buttons and labels, and displays them.

        create_label(text, x, y, font_size=16, text_color="black"):
            Creates a Tkinter label at the specified coordinates with customizable text, font size, and color.

        create_button(command, x, y, pady=0, image_path=None, text=None):
            Creates a button at the specified coordinates with an image or text, and binds it to a command.

        reset_game():
            Resets the game and updates the GUI to reflect the initial state.

        clicked_rock(), clicked_paper(), clicked_scissors():
            Handles the player's choice of Rock, Paper, or Scissors, updates the game state, and refreshes the GUI.

        create_history_label(n=30):
            Displays the last `n` game results in a formatted label, showing rounds, player/AI choices, outcomes, and scores.

        update_results():
            Updates the game's round, win, loss, and tie counters, along with the history and optionally the AI memory matrix and explanation.

        create_ai_explanation_label():
            Displays a label explaining the AI's strategy for choosing moves, particularly in "Smart" mode.

        create_ai_memory_matrix_label():
            Displays a label showing the AI's memory matrix, tracking the player's move patterns across previous rounds.
    """

    def __init__(self, the_game, show_ai):
        """
        Initializes the GUI app with a given game logic and a flag for whether to display AI-related information.

        Args:
            the_game (object): The game object that handles the logic for playing Rock-Paper-Scissors.
            show_ai (bool): Whether to show additional AI information in the GUI.
        """
        self.the_game = the_game
        self.show_ai = show_ai
        self.root = None

        self.app_dimensions = (1000, 625)

        self.main_frame = None
        self.rock_button = None
        self.scissors_button = None
        self.paper_button = None

        self.round_label = None
        self.wins_label = None
        self.losses_label = None
        self.ties_label = None

        self.history_label = None
        self.memory_matrix_label = None

        self.create_app_window()

    def create_app_window(self):
        """
        Creates and configures the main window, sets up the button and label layout,
        and initializes the Rock-Paper-Scissors game UI.
        """
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors")
        self.root.geometry(f"{self.app_dimensions[0]}x{self.app_dimensions[1]}")
        self.root.config(bg="black")

        # Main frame
        self.main_frame = tk.Frame(self.root, bg="white", width=self.app_dimensions[0], height=self.app_dimensions[1])
        self.main_frame.pack_propagate(False)
        self.main_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create game buttons
        self.create_button(self.clicked_rock, x=250, y=60, pady=20, image_path='assets/rock.jpg')
        self.create_button(self.clicked_paper, x=450, y=60, pady=20, image_path='assets/paper.jpg')
        self.create_button(self.clicked_scissors, x=650, y=60, pady=20, image_path='assets/scissors.jpg')
        self.create_button(self.reset_game, x=800, y=15, pady=10, text="Reset")

        # Create labels for rounds and scores
        self.round_label = self.create_label(f"Round: {self.the_game.num_rounds}", 200, 25, font_size=18)
        self.wins_label = self.create_label(f"Wins: {self.the_game.score[0]}", 350, 25, font_size=18)
        self.losses_label = self.create_label(f"Losses: {self.the_game.score[1]}", 500, 25, font_size=18)
        self.ties_label = self.create_label(f"Ties: {self.the_game.score[2]}", 675, 25, font_size=18)

    def create_label(self, text, x, y, font_size=16, text_color="black"):
        """
        Creates a Tkinter label at the specified position with customizable text, font size, and color.

        Args:
            text (str): The text to display on the label.
            x, y (int): The x and y coordinates for placing the label.
            font_size (int): The font size of the text.
            text_color (str): The color of the text (default: "black").

        Returns:
            tk.Label: The created label object.
        """
        label = tk.Label(self.main_frame, text=text, font=tkfont.Font(size=font_size), bg="white", fg=text_color)
        label.place(x=x, y=y)
        return label

    def create_button(self, command, x, y, pady=0, image_path=None, text=None):
        """
        Creates a button at the specified position, either with an image or text, and binds it to a command.

        Args:
            command (callable): The function to be called when the button is pressed.
            x, y (int): The x and y coordinates for placing the button.
            pady (int): Optional padding for the y-axis.
            image_path (str): The file path for the button image (default: None).
            text (str): The text to display on the button (default: None).

        Returns:
            tk.Button: The created button object.
        """
        if image_path:
            img = Image.open(image_path)
            img = img.resize((100, 100), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            button = tk.Button(self.main_frame, image=photo, command=command, padx=0, pady=pady, borderwidth=3,
                               relief="raised",
                               highlightbackground="black", highlightthickness=2)
            button.image = photo  # Keep a reference to avoid garbage collection
        else:
            button = tk.Button(self.main_frame, text=text, command=command, padx=0, pady=pady,
                               font=tkfont.Font(size=15))
        button.place(x=x, y=y)

    def reset_game(self):
        """
        Resets the game to its initial state by calling the game's `init_game` method
        and updates the UI to reflect the reset state.
        """
        self.the_game.init_game()
        self.update_results()

    def clicked_rock(self):
        """
        Handles the player's selection of "Rock", plays a round, and updates the game state in the UI.
        """
        self.the_game.play_round("Rock")
        self.update_results()

    def clicked_paper(self):
        """
        Handles the player's selection of "Paper", plays a round, and updates the game state in the UI.
        """
        self.the_game.play_round("Paper")
        self.update_results()

    def clicked_scissors(self):
        """
        Handles the player's selection of "Scissors", plays a round, and updates the game state in the UI.
        """
        self.the_game.play_round("Scissors")
        self.update_results()

    def create_history_label(self, n=30):
        """
        Creates or updates a label that displays the last `n` game results, showing rounds, player/AI choices, outcomes, and scores.

        Args:
            n (int): The number of rounds to display (default: 30).
        """
        # Get the last n results from history_dict_list, or fewer if there are not enough entries
        last_n_results = self.the_game.history_dict_list[-n:]

        # Create the formatted text for the label
        history_text = "Last 30 Rounds\n"
        for result in reversed(last_n_results):  # Reverse to show the most recent first
            history_text += f"Rounds: {result['num_rounds']}\t"
            history_text += f"Player: {result['player_choice']:>10}\t"
            history_text += f"AI: {result['ai_choice']:>10}\t"
            history_text += f"Outcome: {result['outcome']:>4}\t"
            history_text += f"Score: {result['score'][0]}-{result['score'][1]}-{result['score'][2]}\n"

        # If the label has already been created, update its text
        if self.history_label:
            self.history_label.config(text=history_text)
        else:
            # Create the label if it does not exist
            self.history_label = tk.Label(self.main_frame, text=history_text, anchor='w', justify='left',
                                          bg="white", fg="black", font=tkfont.Font(size=8))
            self.history_label.place(x=25, y=180)

    def update_results(self):
        """
        Updates the game results and refreshes the display by updating round, win, loss, and tie counters.
        If `show_ai` is enabled, it also updates the AI's memory matrix and explanation labels.
        """
        self.round_label.configure(text=f"Round: {self.the_game.num_rounds}")  #
        self.wins_label.configure(text=f"Wins: {self.the_game.score[0]}")  #
        self.losses_label.configure(text=f"Losses: {self.the_game.score[1]}")  #
        self.ties_label.configure(text=f"Ties: {self.the_game.score[2]}")  #
        self.create_history_label()
        if self.show_ai:
            self.create_ai_memory_matrix_label()
            self.create_ai_explanation_label()

        self.root.update()

    def create_ai_explanation_label(self):
        """
        Creates a label that explains the AI's strategy. The AI uses a simple memory-based approach to track the player's
        tendencies and chooses the next move accordingly.
        """
        text = """The AI is making its decision using a very simple form of memory. It is keeping track of how likely 
        you are to choose rock/paper/scissors based on what happened on the previous turn. For example, it is keeping 
        track of what you do the turn after both you and it choose rock at the same time ("rock" vs. "rock" in the table below). 
        Maybe you tended to choose "paper" after a "rock"-"rock" turn. If so, then next time "rock"-"rock" occurs, it will 
        choose "scissors", because you tend to choose "paper" after "rock"-"rock" turns. If there is a tie between your 
        most likely options, it breaks the tie deterministically with a preference for paper, then scissors, then rock, 
        as a tie-breaker. """
        self.ai_explanation_label = tk.Label(self.root, text=text, anchor='w', justify='left',
                                             font=tkfont.Font(size=10), bg="white", fg="black", wraplength=400)
        self.ai_explanation_label.place(x=525, y=200)

    def create_ai_memory_matrix_label(self):
        """
        Creates or updates a label that displays the AI's memory matrix, showing how the AI tracks the player's move patterns.
        The matrix tracks the player's tendencies to choose each move based on prior rounds.
        """
        # Convert index dictionaries back to lists for easier access to labels
        row_labels = list(self.the_game.ai.pair_index_dict.keys())  # Row labels from pair_index_dict
        col_labels = list(self.the_game.ai.move_index_dict.keys())  # Column labels from move_index_dict

        # Add a header for the row labels and column labels
        matrix_text = "Human Choice vs. AI Choice\t\t" + "\t".join(col_labels) + "\n"

        # Add each row with its label and corresponding matrix data
        for row_index, row_label in enumerate(row_labels):
            formatted_row_label = f"{row_label[0]} vs {row_label[1]}"
            row_data = "\t".join(str(val) for val in self.the_game.ai.memory_matrix[row_index])
            matrix_text += f"{formatted_row_label:<25}\t\t{row_data}\n"

        # If the label has already been created, update its text; otherwise, create a new label
        if self.memory_matrix_label:
            self.memory_matrix_label.config(text=matrix_text)
        else:
            self.memory_matrix_label = tk.Label(self.root, text=matrix_text, anchor='w', justify='left',
                                                font=tkfont.Font(size=10), bg="white", fg="black")
            self.memory_matrix_label.place(x=525, y=400)

