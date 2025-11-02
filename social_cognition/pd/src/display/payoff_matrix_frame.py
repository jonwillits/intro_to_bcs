# src/display/payoff_matrix_widget.py
import tkinter as tk
from . import display_styles as S

class PayoffMatrixWidget(tk.Frame):
    def __init__(self, parent, params, bg=None, **kwargs):
        bg = bg or S.COLORS.CONTENT_BG
        super().__init__(parent, bg=bg, **kwargs)

        self.params = params
        w = params.Display.WINDOW_SIZE[0] // 3
        self.config(width=w, height=params.Display.WINDOW_SIZE[1])

        center_w = w // 2
        y_start = 200

        # reuse your labels exactly as you had them
        payoff_matrix_label = tk.Label(self, text="PAYOFF MATRIX", **S.CONTENT_TEXT)
        payoff_matrix_label.place(x=center_w, y=y_start, anchor=tk.N)

        you_label = tk.Label(self, text="You", **S.CONTENT_TEXT)
        you_label.place(x=center_w + 60, y=y_start + 50, anchor=tk.NW)

        you_cooperate_label = tk.Label(self, text="Cooperate", **S.CONTENT_TEXT)
        you_cooperate_label.place(x=center_w - 20, y=y_start + 90, anchor=tk.NW)

        you_defect_label = tk.Label(self, text="Defect", **S.CONTENT_TEXT)
        you_defect_label.place(x=center_w + 100, y=y_start + 90, anchor=tk.NW)

        them_label = tk.Label(self, text="Them", **S.CONTENT_TEXT)
        them_label.place(x=center_w - 180, y=y_start + 150, anchor=tk.NW)

        them_cooperate_label = tk.Label(self, text="Cooperate", **S.CONTENT_TEXT)
        them_cooperate_label.place(x=center_w - 20, y=y_start + 140, anchor=tk.E)

        them_defect_label = tk.Label(self, text="Defect", **S.CONTENT_TEXT)
        them_defect_label.place(x=center_w - 20, y=y_start + 180, anchor=tk.E)

        PM = params.PrisonersDilemma.PAYOFF_MATRIX

        self.cc_label = tk.Label(self, text=f"{PM[1][1]}", **S.CONTENT_TEXT)
        self.cd_label = tk.Label(self, text=f"{PM[1][0]}", **S.CONTENT_TEXT)
        self.dc_label = tk.Label(self, text=f"{PM[0][1]}", **S.CONTENT_TEXT)
        self.dd_label = tk.Label(self, text=f"{PM[0][0]}", **S.CONTENT_TEXT)

        self.cc_label.place(x=center_w, y=y_start + 125, anchor=tk.NW)
        self.cd_label.place(x=center_w, y=y_start + 165, anchor=tk.NW)
        self.dc_label.place(x=center_w + 105, y=y_start + 125, anchor=tk.NW)
        self.dd_label.place(x=center_w + 105, y=y_start + 165, anchor=tk.NW)