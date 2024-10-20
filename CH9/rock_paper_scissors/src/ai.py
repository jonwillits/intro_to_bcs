import random
import numpy as np


class AI:
    """
    A class that simulates the AI opponent in a Rock-Paper-Scissors game.
    The AI can follow different strategies, including random choice, always choosing "Rock," or a "Smart" strategy
    that learns from the player's previous moves using a memory matrix.

    Attributes:
        ai_strategy (str): The strategy the AI uses ('Random', 'Rock', or 'Smart').
        last_player_choice (str): The player's choice from the previous round.
        last_ai_choice (str): The AI's choice from the previous round.
        memory_matrix (np.ndarray): A matrix that tracks the player's behavior based on past move combinations.
        move_index_dict (dict): A dictionary mapping each move ('Rock', 'Paper', 'Scissors') to an index.
        pair_index_dict (dict): A dictionary mapping move combinations (player vs AI choices) to matrix indices.

    Methods:
        init_ai():
            Initializes the AI's memory, resetting previous choices and the memory matrix.

        record_result(player_choice, ai_choice):
            Updates the memory matrix based on the player's and AI's choices from the last round.

        choose_move():
            Determines the AI's next move based on the strategy (Random, Rock, Smart).

        choose_random_move():
            Returns a random choice from 'Rock', 'Paper', or 'Scissors'.
    """

    def __init__(self, ai_strategy):
        """
        Initializes the AI class with a specified strategy and prepares the memory matrix.

        Args:
            ai_strategy (str): The strategy the AI should use ('Random', 'Rock', or 'Smart').
        """
        self.ai_strategy = ai_strategy
        self.last_player_choice = None
        self.last_ai_choice = None
        self.memory_matrix = None

        # Maps player/AI moves to indices for easier access in the memory matrix
        self.move_index_dict = {'Rock': 0, 'Paper': 1, 'Scissors': 2}
        self.pair_index_dict = {('Rock', 'Rock'): 0,
                                ('Rock', 'Paper'): 1,
                                ('Rock', 'Scissors'): 2,
                                ('Paper', 'Rock'): 3,
                                ('Paper', 'Paper'): 4,
                                ('Paper', 'Scissors'): 5,
                                ('Scissors', 'Rock'): 6,
                                ('Scissors', 'Paper'): 7,
                                ('Scissors', 'Scissors'): 8}
        self.init_ai()

    def init_ai(self):
        """
        Initializes the AI by resetting previous choices and clearing the memory matrix.
        The memory matrix is a 9x3 matrix that tracks how often the player chooses each move
        after a given player-AI move combination.
        """
        self.last_player_choice = None
        self.last_ai_choice = None
        self.memory_matrix = np.zeros([9, 3], int)  # Resets the memory matrix

    def record_result(self, player_choice, ai_choice):
        """
        Records the result of the current round into the memory matrix.
        It updates the memory based on the player's move following a particular player-AI move combination.

        Args:
            player_choice (str): The player's move in the current round ('Rock', 'Paper', or 'Scissors').
            ai_choice (str): The AI's move in the current round ('Rock', 'Paper', or 'Scissors').
        """
        if self.last_ai_choice is not None and self.last_player_choice is not None:
            last_choices = (self.last_player_choice, self.last_ai_choice)
            last_choices_index = self.pair_index_dict[last_choices]
            current_choice_index = self.move_index_dict[player_choice]
            # Update the memory matrix for the observed player choice
            self.memory_matrix[last_choices_index, current_choice_index] += 1

        # Update last round's choices for the next round
        self.last_ai_choice = ai_choice
        self.last_player_choice = player_choice

    def choose_move(self):
        """
        Determines the AI's next move based on the selected strategy.

        Returns:
            str: The AI's next move ('Rock', 'Paper', or 'Scissors').
        """
        # Strategy: Random
        if self.ai_strategy == 'Random':
            return self.choose_random_move()

        # Strategy: Always Rock
        elif self.ai_strategy == 'Rock':
            return 'Rock'

        # Strategy: Smart (learns from player behavior using the memory matrix)
        elif self.ai_strategy == 'Smart':
            # If no previous move by the player, default to "Paper"
            if self.last_player_choice is None:
                return "Paper"
            else:
                last_choices = (self.last_player_choice, self.last_ai_choice)
                player_move_history = self.memory_matrix[self.pair_index_dict[last_choices], :]
                player_top_move = np.argmax(player_move_history)  # Find player's most frequent next move

                # Counter the player's predicted next move
                if player_top_move == 0:  # Player likely to choose 'Rock'
                    return 'Paper'
                elif player_top_move == 1:  # Player likely to choose 'Paper'
                    return 'Scissors'
                elif player_top_move == 2:  # Player likely to choose 'Scissors'
                    return 'Rock'

        # Invalid strategy case, fallback to random
        else:
            print(f"Warning: Computer Strategy set improperly to {self.ai_strategy}. Choosing randomly.")
            return self.choose_random_move()

    @staticmethod
    def choose_random_move():
        """
        Chooses a random move from 'Rock', 'Paper', or 'Scissors'.

        Returns:
            str: A randomly selected move.
        """
        print("Random Move")
        return random.choice(['Rock', 'Paper', 'Scissors'])
