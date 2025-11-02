import tkinter as tk

# utils/tooltip_texts.py

TOOLTIPS = {
    # Buttons
    "play.run":        "Run/Pause continuous generations.",
    "play.take_turn":  "Take one full generation (Compete → Select → Reproduce).",
    "play.phase":      "Advance one phase: Compete, then Selection, then Reproduce.",
    "play.reset":      "Reset the world to a fresh random population and generation=0.",

    # Simulation controls
    "sim.rounds": "Rounds per Turn: number of PD rounds per neighbor pair each turn.",
    "sim.keep":   "Proportion to Keep: fraction [0–1] of highest-scoring agents that survive.",
    "sim.noise":  "AI Noise: probability an AI flips its intended move.",

    # Legend
    "legend.panel": "Live counts of each AI type currently in the world.",

    # Grid
    "grid.cell": "Each square shows an agent’s type (by color) and its current score.",

    # play tab tooltips
    "play.noise":     "AI Noise: probability an AI flips its intended move based on its strategy (0–1).",
    "play.cooperate": "Play a round choosing Cooperate. The AI will respond based on its strategy (plus noise).",
    "play.defect":    "Play a round choosing Defect. Useful for probing retaliation/forgiveness.",
    "play.reset":     "Reset scores and histories in Play. Also restores AI Noise to the default from params.",
}

class ToolTip:
    def __init__(self, widget, text, delay_ms=350):
        self.widget = widget
        self.text = text
        self.delay_ms = delay_ms
        self.tip_window = None
        self._after_id = None

        try:
            widget.bind("<Enter>", self._on_enter)
        except AttributeError:
            print("")
        widget.bind("<Leave>", self._on_leave)
        widget.bind("<ButtonPress>", self._on_leave)  # hide on click

    def _on_enter(self, _event=None):
        # start delayed show
        if self._after_id is None:
            self._after_id = self.widget.after(self.delay_ms, self._show_tip)

    def _on_leave(self, _event=None):
        # cancel delayed show / hide if visible
        if self._after_id is not None:
            self.widget.after_cancel(self._after_id)
            self._after_id = None
        self._hide_tip()

    def _show_tip(self):
        self._after_id = None
        if self.tip_window or not self.text:
            return

        x = self.widget.winfo_rootx() + 12
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 6

        tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)            # no window chrome
        tw.wm_geometry(f"+{x}+{y}")
        self.tip_window = tw

        label = tk.Label(
            tw, text=self.text, justify="left",
            bg="#FFFFDD", relief="solid", borderwidth=1, fg="black",
            padx=6, pady=3, font=("Arial", 9)
        )
        label.pack()

    def _hide_tip(self):
        if self.tip_window is not None:
            self.tip_window.destroy()
            self.tip_window = None

def attach_tooltip(widget, key, default_text=""):
    """Attach tooltip by registry key; if missing, uses default_text (or no-op)."""
    text = TOOLTIPS.get(key, default_text)
    if text:
        ToolTip(widget, text)