import tkinter as tk
from . import display_styles as S
from ..prisoners_dilemma import conduct_tournament
from . import payoff_matrix_frame

class TournamentView:

    def __init__(self, parent, roster, small_image_dict, params):
        self.parent = parent
        self.roster = roster  # {name: AI_instance}
        self.names = list(self.roster.keys())
        self.params = params
        self.small_image_dict = small_image_dict
        self.image_size = 50
        self.names = list(self.roster.keys())

        self.tournament_frame = None
        self.payoff_matrix_frame = None
        self.rounds_label = None
        self.rounds_entry = None
        self.btn_go = None
        self.btn_reset = None
        self.table = None

        self.image_dict = None
        self.results_label = None
        self.row_labels_frame = None
        self.column_labels_frame = None
        self.score_labels_frame = None
        self.score_label_matrix = None

        self.start_y = 100
        self.center_x = self.params.Display.WINDOW_SIZE[0]//2
        self.reset_players()
        for name in self.roster:
            print(name)
            for opponent in self.roster[name].opponent_score_dict:
                print(opponent)

        self._defaults = {
            "AI_NOISE": getattr(self.params.AI, "NOISE", getattr(self.params.AI, "noise", 0.0)),
            "NUM_ROUNDS": getattr(self.params.Tournament, "NUM_ROUNDS", getattr(self.params.Tournament, "NUM_ROUNDS", 1.0)),
        }

    def reset_players(self):
        for ai_name in self.roster:
            self.roster[ai_name].reset_history()
            for name1 in self.roster:
                for name2 in self.roster:
                    if name2 not in self.roster[name1].opponent_score_dict:
                        self.roster[name1].opponent_score_dict[name2] = []

    # ---------- UI ----------
    def mount(self):
        self.create_payoff_matrix_frame()
        self.create_tournament_frame()

    def create_payoff_matrix_frame(self):
        self.payoff_matrix = payoff_matrix_frame.PayoffMatrixWidget(self.parent, self.params)
        self.payoff_matrix.place(x=0, y=0)

    def create_tournament_frame(self):
        x = self.params.Display.WINDOW_SIZE[0] // 3
        w = 2 * (self.params.Display.WINDOW_SIZE[0] // 3)  # left third
        h = self.params.Display.WINDOW_SIZE[1]
        center_x = w //2
        y_start = 100

        self.tournament_frame = tk.Frame(self.parent, bg=S.COLORS.CONTENT_BG)
        self.tournament_frame.place(x=x, y=0, width=w, height=h, anchor=tk.NW)

        # Controls row
        self.rounds_label = tk.Label(self.tournament_frame, text="# Rounds:", **S.CONTENT_TEXT)
        self.rounds_label.place(x=center_x-250, y=y_start, anchor="w")

        self.rounds_entry = tk.Entry(self.tournament_frame, **S.CONTENT_TEXT_ENTRY)
        self.rounds_entry.place(x=center_x-150, y=y_start, width=80, height=26, anchor="w")
        self.rounds_entry.insert(0, self.params.Tournament.NUM_ROUNDS)

        self.btn_go = tk.Button(self.tournament_frame, text="Go", command=self.on_go, **S.CONTENT_BUTTON)
        self.btn_go.place(x=center_x+10, y=y_start, anchor="w")

        self.btn_reset = tk.Button(self.tournament_frame, text="Reset", command=self.on_reset, **S.CONTENT_BUTTON)
        self.btn_reset.place(x=center_x+150, y=y_start, anchor="w")

        # --- AI Noise ---
        self.noise_label = tk.Label(self.tournament_frame, text="AI Noise", **S.CONTENT_TEXT)
        self.noise_label.place(x=center_x-250, y=y_start+30, anchor="w")

        self.noise_entry = tk.Entry(self.tournament_frame, **S.CONTENT_TEXT_ENTRY)
        self.noise_entry.place(x=center_x-150, y=y_start+30, width=80, height=26, anchor="w")
        self.noise_entry.insert(0, self.params.AI.NOISE)

        self.create_results_table(center_x, y_start)

    def create_results_table(self, center_x, start_y):
        self.results_label = tk.Label(self.tournament_frame, text="RESULTS:", **S.CONTENT_TEXT)
        self.results_label.place(x=center_x, y=start_y+70, anchor="w")
        self.score_label_matrix = []

        image_padding = 20
        num_images = len(self.roster)
        header_size = self.image_size*num_images + image_padding*(num_images-1)

        self.row_labels_frame = tk.Frame(self.tournament_frame, bg=S.COLORS.CONTENT_BG)
        self.row_labels_frame.place(x=center_x-100,
                                    y=start_y+120,
                                    width=header_size, height=self.image_size, anchor=tk.NW)

        self.column_labels_frame = tk.Frame(self.tournament_frame, bg=S.COLORS.CONTENT_BG)
        self.column_labels_frame.place(x=center_x-100-self.image_size-image_padding,
                                       y=start_y+120+self.image_size+image_padding,
                                       width=self.image_size, height=header_size, anchor=tk.NW)

        self.score_labels_frame = tk.Frame(self.tournament_frame, bg=S.COLORS.CONTENT_BG)
        self.score_labels_frame.place(x=center_x-100,
                                       y=start_y+120+self.image_size+image_padding,
                                       width=header_size, height=header_size, anchor=tk.NW)

        print(self.roster)
        for i, name1 in enumerate(self.roster):
            xi = i * (self.image_size + image_padding)

            row_image_label = tk.Label(self.row_labels_frame, bg=S.COLORS.CONTENT_BG)
            row_image_label.place(x=xi, y=0, anchor=tk.NW)
            row_image_label.config(image=self.small_image_dict[name1], text="")

            column_image_label = tk.Label(self.column_labels_frame, bg=S.COLORS.CONTENT_BG)
            column_image_label.place(x=0, y=xi, anchor=tk.NW)
            column_image_label.config(image=self.small_image_dict[name1], text="")

            self.score_label_matrix.append([])

            for j, name2, in enumerate(self.roster):
                yi = j * (self.image_size + image_padding)

                score_label = tk.Label(self.score_labels_frame,
                                       text=self.roster[name1].opponent_score_dict[name2],
                                       anchor="center",
                                       **S.TOURNAMENT_SCORE_TEXT)
                score_label.place(x=xi+20, y=yi+20, anchor=tk.NW)
                self.score_label_matrix[i].append(score_label)

    def update_results_table(self):
        for i, name1 in enumerate(self.roster):
            for j, name2, in enumerate(self.roster):
                self.score_label_matrix[i][j].config(text=self.roster[name1].opponent_score_dict[name2])

    def destroy(self):
        # Display will clear children; no extra teardown required
        pass

    # ---------- Behavior ----------
    def update_params(self):
        # AI Noise (float in [0,1]), set on params and all current agents
        try:
            noise = float(self.noise_entry.get())
            noise = 0.0 if noise < 0 else (1.0 if noise > 1.0 else noise)
        except Exception:
            raise Exception("NOISE problem")
        if hasattr(self.params.AI, "NOISE"):
                self.params.AI.NOISE = noise
        for agent in self.roster:
            self.roster[agent].noise = noise

    def on_go(self):
        try:
            rounds = int(self.rounds_entry.get())
            if rounds <= 0:
                raise ValueError
        except Exception:
            # gentle fallback
            rounds = 50
            self.rounds_entry.delete(0, tk.END)
            self.rounds_entry.insert(0, str(rounds))
        self.update_params()

        self.run_tournament(num_rounds=rounds)
        self.update_results_table()

    def on_reset(self):
        self.reset_players()
        self.update_results_table()

    def run_tournament(self, num_rounds):
        conduct_tournament(self.roster, num_rounds, self.params.PrisonersDilemma.PAYOFF_MATRIX)