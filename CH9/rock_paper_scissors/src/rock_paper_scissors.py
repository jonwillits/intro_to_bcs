import copy


class RockPaperScissors:
    """
    A class that simulates the Rock-Paper-Scissors game, allowing a human player to play against an AI opponent.
    The game keeps track of rounds, scores, player and AI choices, and game history.

    Attributes:
        ai (object): The AI opponent that implements the logic for choosing moves and recording results.
        num_rounds (int): The total number of rounds played.
        score (list of int): The game score represented as a list in the format [wins, losses, ties].
        player_choice (str): The player's choice for the current round ('Rock', 'Paper', or 'Scissors').
        ai_choice (str): The AI's choice for the current round.
        outcome (str): The outcome of the current round ('Win', 'Lose', 'Tie').
        history_dict_list (list of dict): A list of dictionaries, each representing the history of a round.

    Methods:
        init_game():
            Initializes the game by resetting the number of rounds, score, and history, and initializing the AI.

        determine_outcome():
            Determines the outcome of the current round based on player and AI choices.

        play_round(player_choice):
            Executes a round by recording player and AI choices, determining the outcome, updating the score, and
            saving the round result to the history.

        update_score():
            Updates the score based on the outcome of the current round.

        add_outcome_to_history():
            Saves the details of the current round (choices, outcome, score, etc.) into the history.

        print_round():
            Prints the results of the current round, including choices, outcome, and updated score.
    """

    def __init__(self, ai):
        """
        Initializes the RockPaperScissors class with the AI instance and sets the game state to None or empty.

        Args:
            ai (object): The AI opponent object which must have `choose_move()` and `record_result()` methods.
        """
        self.ai = ai

        self.num_rounds = None
        self.score = None
        self.player_choice = None
        self.ai_choice = None
        self.outcome = None
        self.history_dict_list = None

        self.init_game()

    def init_game(self):
        """
        Initializes the game by resetting the number of rounds, score, and player/AI choices.
        It also initializes the AI opponent for a fresh start.
        """
        self.num_rounds = 0
        self.score = [0, 0, 0]  # [wins, losses, ties]
        self.player_choice = None
        self.ai_choice = None
        self.outcome = None
        self.history_dict_list = []
        self.ai.init_ai()

    def determine_outcome(self):
        """
        Determines the outcome of the current round based on the player's choice and the AI's choice.

        Returns:
            str: The result of the round ('Win', 'Lose', 'Tie').
        """
        outcomes = {
            ('Rock', 'Rock'): 'Tie',
            ('Rock', 'Paper'): 'Lose',
            ('Rock', 'Scissors'): 'Win',
            ('Paper', 'Rock'): 'Win',
            ('Paper', 'Paper'): 'Tie',
            ('Paper', 'Scissors'): 'Lose',
            ('Scissors', 'Rock'): 'Lose',
            ('Scissors', 'Paper'): 'Win',
            ('Scissors', 'Scissors'): 'Tie',
        }
        outcome = outcomes.get((self.player_choice, self.ai_choice), "Invalid")
        return outcome

    def play_round(self, player_choice):
        """
        Plays a round of Rock-Paper-Scissors by recording the player's choice, generating the AI's choice,
        determining the outcome, updating the score, and saving the result to the game history.

        Args:
            player_choice (str): The player's move ('Rock', 'Paper', or 'Scissors').
        """
        self.player_choice = player_choice
        self.ai_choice = self.ai.choose_move()
        self.ai.record_result(self.player_choice, self.ai_choice)
        self.outcome = self.determine_outcome()
        self.update_score()
        self.add_outcome_to_history()
        self.print_round()

    def update_score(self):
        """
        Updates the game score based on the outcome of the current round.
        Increments the respective score category (wins, losses, ties) and increments the number of rounds.
        """
        if self.outcome == 'Win':
            self.score[0] += 1
        elif self.outcome == 'Lose':
            self.score[1] += 1
        elif self.outcome == 'Tie':
            self.score[2] += 1
        self.num_rounds += 1

    def add_outcome_to_history(self):
        """
        Adds the details of the current round (player choice, AI choice, outcome, and score) to the history.
        """
        outcome_dict = {"player_choice": self.player_choice,
                        "ai_choice": self.ai_choice,
                        "outcome": self.outcome,
                        "num_rounds": self.num_rounds,
                        "score": copy.copy(self.score)}
        self.history_dict_list.append(outcome_dict)

    def print_round(self):
        """
        Prints the results of the current round, including the round number, player and AI choices,
        outcome of the round, and the updated score.
        """
        output_string = f"Rounds: {self.num_rounds:<3}"
        output_string += f"Player: {self.player_choice:<10}"
        output_string += f"AI: {self.ai_choice:<10}"
        output_string += f"Outcome: {self.outcome:<10}"
        output_string += f"Score: {self.score[0]}-{self.score[1]}-{self.score[2]}"
        print(output_string)
