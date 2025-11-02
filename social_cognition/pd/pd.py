# one_v_one.py (top level)
import params
from src.players import HumanPlayer, RandomAI, NiceAI, MeanAI, TitForTatAI, WinStayLoseShiftAI
from src.display.display import Display
from src.prisoners_dilemma import conduct_tournament

def build_roster(params_obj):
    tuples = [
        ("Michael", RandomAI),
        ("Kevin",   NiceAI),
        ("Angela",  MeanAI),
        ("Pam",     TitForTatAI),
        ("Oscar",   WinStayLoseShiftAI)
    ]

    roster = {}
    for name, player_class in tuples:
        roster[name] = player_class(params_obj, name)
    name_list = list(roster.keys())
    for i, name1 in enumerate(name_list):
        for j, name2 in enumerate(name_list):
            if name2 not in roster[name1].opponent_score_dict:
                roster[name1].opponent_score_dict[name2] = []

    return {name: cls(params_obj, name) for name, cls in tuples}

def headless_tournament_demo(params_obj, roster):
    conduct_tournament(roster, params_obj.Tournament.NUM_ROUNDS, params_obj.PrisonersDilemma.PAYOFF_MATRIX)
    print_table(roster)

def print_table(roster):
    name_list = list(roster.keys())

    col_width = 21
    header = " " * (col_width) + "".join(f"{name:>{col_width}}" for name in name_list)
    print(header)
    for r in range(len(name_list)):
        row_label = name_list[r]
        row_cells = [f"{row_label:>{col_width}}"]
        current_player_name= name_list[r]
        current_player = roster[current_player_name]

        for c in range(len(name_list)):
            opponent_name = name_list[c]
            if opponent_name in current_player.opponent_score_dict:
                opponent_score = current_player.opponent_score_dict[opponent_name]
            else:
                opponent_score = "-"
            row_cells.append(f"{opponent_score:>{col_width}}")
        print("".join(row_cells))


def run_gui(params_obj, roster):

    human = HumanPlayer("You")
    ui = Display(params_obj,
                 roster=roster,
                 human=human,
                 images_dir="images")
    ui.run()

def main():
    roster = build_roster(params)
    headless = False  # flip this to False when you want the GUI
    if headless:
        headless_tournament_demo(params, roster)
    else:
        run_gui(params, roster)

if __name__ == "__main__":
    main()