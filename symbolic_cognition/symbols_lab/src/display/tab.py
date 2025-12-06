# src/display/tab.py

import tkinter as tk

class Tab(tk.Frame):
    """
    Base class for all tabs.
    Subclasses should:
      - Build widgets in __init__
      - Optionally override on_show / on_hide
    """

    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, **kwargs)
        self.controller = controller  # typically the Display instance

    def on_show(self):
        """Called when this tab becomes visible."""
        pass

    def on_hide(self):
        """Called when this tab is hidden."""
        pass


# ----- Example tab implementations -----
# You can delete these and add your own for each app.

class HomeTab(Tab):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, controller, **kwargs)
        label = tk.Label(self, text="Home Tab", font=("Helvetica", 16))
        label.pack(padx=20, pady=20)


class SettingsTab(Tab):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, controller, **kwargs)
        label = tk.Label(self, text="Settings Tab", font=("Helvetica", 16))
        label.pack(padx=20, pady=20)


# List of (label, TabClass) pairs that Display will use to build its menu.
# You can override this per project if you like.
TAB_SPECS = [
    ("Home", HomeTab),
    ("Settings", SettingsTab),
]