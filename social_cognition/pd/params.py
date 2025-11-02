class GeneralParams:
    RANDOM_SEED = None

class Tournament:
    NUM_ROUNDS = 1

class Display:
    WINDOW_SIZE = (1280, 720)

class PrisonersDilemma:
    REWARD_MUTUAL_COOP = 3
    EXPLOITER = 5
    SUCKER = 0
    PUNISH_MUTUAL_DEFECT = 1
    PAYOFF_MATRIX = [[(PUNISH_MUTUAL_DEFECT, PUNISH_MUTUAL_DEFECT), (EXPLOITER, SUCKER)],
                     [(SUCKER, EXPLOITER), (REWARD_MUTUAL_COOP, REWARD_MUTUAL_COOP)]]

class AI:
    NOISE = 0.00

class EvolutionarySimulation:
    AI_FREQ_DICT = {'NiceAI': 1,
                    'MeanAI': 1,
                    'RandomAI': 1,
                    'TitForTatAI': 1,
                    'WinStayLoseShiftAI': 0}
    ROUNDS_PER_TURN = 5
    PROPORTION_TO_KEEP = 0.5