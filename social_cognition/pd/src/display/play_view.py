# src/play_pd.py
import tkinter as tk
from . import display_styles as S
from . import payoff_matrix_frame
from ..prisoners_dilemma import resolve_round
from .tooltips import attach_tooltip

COOPERATE = 1
DEFECT = 0

class PlayView:

    def __init__(self, parent, roster, human, images_dict, params):
        self.parent = parent          # the content_frame
        self.roster = roster          # dict {name: AI_instance}
        self.human = human
        self.images_dict = images_dict
        self.params = params

        self.names = list(self.roster.keys())
        self.current_partner = self.names[0]
        self._current_photo = None

        self.payoff_matrix_frame = None
        self.btn_coop = None
        self.btn_def = None
        self.btn_reset = None

        self.play_frame = None
        self.name_label = None
        self.image_label = None
        self.partner_var = None
        self.partner_menu = None

        self.results_frame = None
        self.result_label = None
        self.totals_label = None

    def create_payoff_matrix_frame(self):
        self.payoff_matrix_frame = payoff_matrix_frame.PayoffMatrixWidget(self.parent, self.params)
        self.payoff_matrix_frame.place(x=0, y=0)

    def create_play_frame(self):
        w = self.params.Display.WINDOW_SIZE[0] // 3  # left third
        h = self.params.Display.WINDOW_SIZE[1]
        center_w = w //2
        y_start = 100

        self.play_frame = tk.Frame(self.parent, bg=S.COLORS.CONTENT_BG)
        self.play_frame.place(x=w, y=0, width=w, height=h, anchor=tk.NW)

        partner_label = tk.Label(self.play_frame, text="Partner:", **S.CONTENT_TEXT)
        partner_label.place(x=center_w, y=y_start, anchor=tk.N)

        self.partner_var = tk.StringVar(self.play_frame, value=self.current_partner)
        self.partner_menu = tk.OptionMenu(self.play_frame, self.partner_var, *self.names)
        self.partner_menu.place(x=center_w, y=y_start+40, anchor=tk.N)
        S.apply_optionmenu_style(self.partner_menu, S.OPTIONMENU)
        self.partner_var.trace_add("write", self.on_partner_changed)

        # Portrait
        self.image_label = tk.Label(self.play_frame, bg=S.COLORS.CONTENT_BG)
        self.image_label.place(x=center_w, y=y_start+80, anchor=tk.N)

        # Buttons
        self.btn_coop = tk.Button(
            self.play_frame, text="Cooperate",
            command=lambda: self.play_round(COOPERATE),
            **S.CONTENT_BUTTON
        )
        self.btn_coop.place(x=center_w-120, y=y_start+320, anchor=tk.NW)

        self.btn_def = tk.Button(
            self.play_frame, text="Defect",
            command=lambda: self.play_round(DEFECT),
            **S.CONTENT_BUTTON
        )
        self.btn_def.place(x=center_w+20, y=y_start + 320, anchor=tk.NW)

        self.btn_reset = tk.Button(
            self.play_frame, text="Reset",
            command=lambda: self.reset(),
            **S.CONTENT_BUTTON
        )
        self.btn_reset.place(x=center_w, y=y_start + 400, anchor=tk.N)

        attach_tooltip(self.btn_coop, "play.cooperate")
        attach_tooltip(self.btn_def, "play.defect")
        attach_tooltip(self.btn_reset, "play.reset")

    def create_results_frame(self):
        w = self.params.Display.WINDOW_SIZE[0] // 3  # left third
        h = self.params.Display.WINDOW_SIZE[1]
        center_w = w //2
        y_start = 100

        self.results_frame = tk.Frame(self.parent, bg=S.COLORS.CONTENT_BG)
        self.results_frame.place(x=w*2, y=0, width=w, height=h, anchor=tk.NW)

        # Result + totals
        self.result_label = tk.Label(self.results_frame, text="", **S.CONTENT_TEXT)
        self.result_label.place(x=center_w, y=y_start, anchor="n")

        totals_text = self.update_totals_text()

        self.totals_label = tk.Label(self.results_frame, text=totals_text, **S.CONTENT_TEXT)
        self.totals_label.config(justify="left")
        self.totals_label.place(x=center_w, y=y_start+200, anchor="n")

    def mount(self):
        self.create_payoff_matrix_frame()
        self.create_play_frame()
        self.create_results_frame()

        # initialize state
        self.apply_partner(self.current_partner)

    def reset(self):
        self.human.reset_history()
        for ai_name in self.roster:
            self.roster[ai_name].reset_history()
        totals_text = self.update_totals_text()
        self.totals_label.config(text=totals_text)
        self.result_label.config(text="")
        self.payoff_matrix_frame.cc_label.config(bg="#FFFFFF")
        self.payoff_matrix_frame.dd_label.config(bg="#FFFFFF")
        self.payoff_matrix_frame.cd_label.config(bg="#FFFFFF")
        self.payoff_matrix_frame.dc_label.config(bg="#FFFFFF")

    def update_totals_text(self):
        totals_text = f"Total Points:\n"
        totals_text += f"You: {self.human.score}\n"
        for ai_name in self.roster:
            totals_text += f"{ai_name}: {self.roster[ai_name].score}\n"
        return totals_text

    def destroy(self):
        # widgets will be destroyed by Display; no extra teardown needed
        pass

    def on_partner_changed(self, *_):
        self.apply_partner(self.partner_var.get())

    def apply_partner(self, name: str):
        self.current_partner = name
        self.image_label.config(image=self.images_dict[name], text="")

    def play_round(self, human_move: int):
        partner = self.current_partner
        agent = self.roster.get(partner)
        if agent is None:
            self.result_label.config(text=f"[Error] No agent named '{partner}' in roster")
            return

        ai_move = agent.choose_move(self.human.name)

        human_result, ai_result = resolve_round(human_move, ai_move, self.params.PrisonersDilemma.PAYOFF_MATRIX)
        # record in both histories
        self.human.record_interaction(
            opponent_name=partner,
            my_move=human_move,
            their_move=ai_move,
            my_outcome=human_result,
            their_outcome=ai_result,
        )
        agent.record_interaction(
            opponent_name=self.human.name,
            my_move=ai_move,
            their_move=human_move,
            my_outcome=ai_result,
            their_outcome=human_result,
        )

        label_list = ["Defect", "Cooperate"]

        result_text = f"RESULT:\n\n"
        result_text += f"Your Move: {label_list[human_move]}\n"
        result_text += f"{partner}'s Move: {label_list[ai_move]}\n\n"
        result_text += f"Your Result: {human_result}\n"
        result_text += f"{partner}'s Result: {ai_result}"

        self.result_label.config(text=result_text)
        totals_text = self.update_totals_text()
        self.totals_label.config(text=totals_text)

        self.payoff_matrix_frame.cc_label.config(bg="#FFFFFF")
        self.payoff_matrix_frame.cd_label.config(bg="#FFFFFF")
        self.payoff_matrix_frame.dc_label.config(bg="#FFFFFF")
        self.payoff_matrix_frame.dd_label.config(bg="#FFFFFF")
        if ai_move and human_move:
            self.payoff_matrix_frame.cc_label.config(bg="#BBBBBB")
        elif ai_move and not human_move:
            self.payoff_matrix_frame.dc_label.config(bg="#BBBBBB")
        elif not ai_move and human_move:
            self.payoff_matrix_frame.cd_label.config(bg="#BBBBBB")
        else:
            self.payoff_matrix_frame.dd_label.config(bg="#BBBBBB")