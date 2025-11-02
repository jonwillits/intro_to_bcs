# src/ai.py
import random

COOPERATE = 1
DEFECT    = 0

class Player:
    """Concrete base for all players (human or AI)."""

    def __init__(self, name: str, params=None):
        self.name: str = name
        self.score: int = 0  # running total
        self.player_type = None

        # History per opponent: list of dicts with what happened each round
        # e.g., {"me": COOPERATE, "them": DEFECT, "my_outcome": -3, "their_outcome": 3}
        self.history = {}
        self.opponent_score_dict = {}

    def record_interaction(self, opponent_name, my_move, their_move, my_outcome, their_outcome):
        self.score += my_outcome

        if opponent_name not in self.history:
            self.history[opponent_name] = []
            self.opponent_score_dict[opponent_name] = 0

        self.history[opponent_name].append({
                "my_move": my_move,
                "their_move": their_move,
                "my_outcome": my_outcome,
                "their_outcome": their_outcome,
            }
        )
        self.opponent_score_dict[opponent_name] += my_outcome

    def last_interaction(self, opponent_name: str):
        """Return the last history dict vs this opponent, or None."""
        seq = self.history.get(opponent_name, [])
        return seq[-1] if seq else None

    def choose_move(self, opponent_name: str) -> int:
        """Humans don't auto-choose; GUI should pass human moves directly."""
        raise NotImplementedError("Human/AI subclasses implement move choice.")

    def reset_history(self):
        self.history = {}
        self.opponent_score_dict = {}
        self.score = 0

class HumanPlayer(Player):
    def __init__(self, params, name="Human"):
        super().__init__(name, params=params)
        self.player_type = "Human"

    """Human player: GUI should supply their move directly; no auto-choice here."""
    def choose_move(self, opponent_name: str) -> int:
        raise RuntimeError("Human moves are provided by the UI; do not call choose_move().")


# -------------------------
# AI base (adds noise)
# -------------------------
class BaseAI(Player):
    """Base for AI strategies. Applies 'noise' by flipping the chosen move with some probability."""

    def __init__(self, params, name):
        super().__init__(name, params=params)
        # Pull noise from params; default to 0 if absent
        self.noise = params.AI.NOISE
        self.player_type = "BaseAI"

    # ---- Helpers ----
    @staticmethod
    def flip(move):
        return COOPERATE if move == DEFECT else DEFECT

    def apply_noise(self, move):

        """Flip the move with probability = self.noise."""
        if not (0.0 <= self.noise <= 1.0):
            return move  # be forgiving if params are weird
        else:
            if random.random() < self.noise:
                return self.flip(move)
            else:
                return move

    # Subclasses implement this to provide the base (deterministic) choice
    def base_choice(self, opponent_name):
        raise NotImplementedError

    # Public choice: base strategy, then noise flip
    def choose_move(self, opponent_name):
        base = self.base_choice(opponent_name)

        move = self.apply_noise(base)
        return move


# -------------------------
# Concrete AI strategies
# -------------------------
class RandomAI(BaseAI):
    """Ignores history and picks randomly every round."""
    def __init__(self, params, name="RandomAI"):
        super().__init__(params, name)
        self.player_type = "RandomAI"

    def base_choice(self, opponent_name):
        return random.choice([COOPERATE, DEFECT])


class NiceAI(BaseAI):
    """Always cooperates (then noise may flip)."""
    def __init__(self, params, name="NiceAI"):
        super().__init__(params, name)
        self.player_type = "NiceAI"

    def base_choice(self, opponent_name):
        return COOPERATE

class MeanAI(BaseAI):
    """Always defects (then noise may flip)."""
    def __init__(self, params, name="MeanAI"):
        super().__init__(params, name)
        self.player_type = "MeanAI"

    def base_choice(self, opponent_name):
        return DEFECT

class TitForTatAI(BaseAI):
    """Cooperate on first encounter; thereafter mirror the opponent's last move."""
    def __init__(self, params, name="TitForTatAI"):
        super().__init__(params, name)
        self.player_type = "TitForTatAI"

    def base_choice(self, opponent_name):
        last = self.last_interaction(opponent_name)
        if last is None:
            return COOPERATE
        return last["their_move"]

class WinStayLoseShiftAI(BaseAI):
    """
    If last round's outcome for ME was positive, repeat my last move (stay).
    If last round's outcome for ME was negative or zero, switch (shift).
    """
    def __init__(self, params, name="WinStayLoseShiftAI"):
        super().__init__(params, name)
        self.player_type = "WinStayLoseShiftAI"
        self.win_threshold = params.PrisonersDilemma.PUNISH_MUTUAL_DEFECT

    def base_choice(self, opponent_name):
        last = self.last_interaction(opponent_name)
        if last is None:
            return COOPERATE  # simple, friendly start

        last_my_move = last["my_move"]
        last_my_outcome = last["my_outcome"]

        # Define "win" simply as > 0; adjust if you use a different payoff scaling.
        win = last_my_outcome > self.win_threshold
        return last_my_move if win else self.flip(last_my_move)