# src/display/display.py

import tkinter as tk
from . import display_styles as S
from . import tab as tab_module


class Display:
    def __init__(self, params):
        self.params = params
        self.W, self.H = params.Display.WINDOW_SIZE

        # Root window
        self.root = tk.Tk()
        self.root.title(params.Display.TITLE)
        self.root.geometry(f"{self.W}x{self.H}")

        # Top-level frames
        self.menu_frame = None
        self.menu_left = None
        self.menu_right = None
        self.content_frame = None

        # Tabs and buttons
        self.tabs = {}          # name -> Tab instance
        self.tab_buttons = {}   # name -> Button instance
        self.current_tab_name = None

        self.quit_button = None

        self._build_layout()
        self._create_tabs_from_tab_module()

        # Show first tab by default (if any)
        if self.tabs:
            first_name = next(iter(self.tabs.keys()))
            self.show_tab(first_name)

    # ---------- Layout ----------

    def _build_layout(self):
        # Menu frame at top
        self.menu_frame = tk.Frame(
            self.root,
            height=self.params.Display.MENU_HEIGHT,
            bg=S.MENU_BG,
        )
        self.menu_frame.pack(side=tk.TOP, fill=tk.X)

        # Left/right subframes: left for tab buttons, right for Quit
        self.menu_left = tk.Frame(self.menu_frame, bg=S.MENU_BG)
        self.menu_left.pack(side=tk.LEFT, fill=tk.Y)

        self.menu_right = tk.Frame(self.menu_frame, bg=S.MENU_BG)
        self.menu_right.pack(side=tk.RIGHT, fill=tk.Y)

        # Content frame fills the rest
        self.content_frame = tk.Frame(self.root, bg=S.CONTENT_BG)
        self.content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Make content_frame a single grid cell that stretches
        self.content_frame.rowconfigure(0, weight=1)
        self.content_frame.columnconfigure(0, weight=1)

        # Quit button on the right
        self.quit_button = tk.Button(
            self.menu_right,
            text="Quit",
            command=self.quit,
            bg=S.QUIT_BUTTON_BG,
            fg=S.QUIT_BUTTON_FG,
            relief=tk.RAISED,
        )
        self.quit_button.pack(side=tk.RIGHT, padx=8, pady=4)

    # ---------- Tabs ----------

    def _create_tabs_from_tab_module(self):
        """
        Create tabs and corresponding buttons based on tab_module.TAB_SPECS.
        TAB_SPECS should be a list of (label, TabClass) pairs.
        """
        for name, TabClass in getattr(tab_module, "TAB_SPECS", []):
            # Create tab instance and grid it in the same cell (stacked)
            tab_instance = TabClass(
                self.content_frame,
                controller=self,
                bg=S.CONTENT_BG,
            )
            tab_instance.grid(row=0, column=0, sticky="nsew")
            self.tabs[name] = tab_instance

            # Create button for the tab
            btn = tk.Button(
                self.menu_left,
                text=name,
                bg=S.BUTTON_BG,
                fg=S.BUTTON_FG,
                activebackground=S.BUTTON_ACTIVE_BG,
                relief=tk.RAISED,
                command=lambda n=name: self.show_tab(n),
            )
            btn.pack(side=tk.LEFT, padx=4, pady=4)
            self.tab_buttons[name] = btn

    # ---------- View switching ----------

    def show_tab(self, name: str):
        """Hide current tab (logically), bring requested one to front."""
        if name not in self.tabs:
            return

        # If we're already on that tab, do nothing
        if self.current_tab_name == name:
            return

        # Call on_hide on old tab
        if self.current_tab_name is not None:
            old_tab = self.tabs[self.current_tab_name]
            if hasattr(old_tab, "on_hide"):
                old_tab.on_hide()

        # Raise new tab
        new_tab = self.tabs[name]
        new_tab.tkraise()

        if hasattr(new_tab, "on_show"):
            new_tab.on_show()

        self.current_tab_name = name

    # ---------- App control ----------

    def quit(self):
        self.root.quit()
        self.root.destroy()

    def run(self):
        self.root.mainloop()