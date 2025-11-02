# src/one_v_one_display.py
import os
import sys
import tkinter as tk
from . import display_styles as S
from .play_view import PlayView
from .tournament_view import TournamentView
from .simulation_view import SimulationView


class Display:
    """
    Shell UI:
      - Top menu bar with three buttons: Play, Tournament, Simulation
      - Content area where a single "view" (PlayView / TournamentView / SimulationView) is mounted
    """

    def __init__(self, params, roster, human, images_dir="images"):
        # window size from params

        self.W, self.H = params.Display.WINDOW_SIZE
        self.roster = roster
        self.human = human
        self.menu_height = 40
        self.params = params

        # images path relative to run script
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.images_dir = os.path.join(script_dir, images_dir)
        self.images_dict = {}
        self.small_images_dict = {}
        self.mini_images_dict = {}

        # Tk root + frames
        self._create_main_window()

        self.load_images()

        # menu + content
        self._create_menu()
        self._create_content()

        # current view (mount Play by default)
        self.current_view = None
        self.show_play_view()

        self.root.protocol("WM_DELETE_WINDOW", self.quit)

    # ---------- Window ----------
    def _create_main_window(self):
        self.root = tk.Tk()
        self.root.title("Prisoner's Dilemma")
        self.root.geometry(f"{self.W}x{self.H}")
        self.root.resizable(False, False)

        self.menu_frame = tk.Frame(self.root, bg=S.COLORS.MENU_BG)
        self.menu_frame.place(x=0, y=0, width=self.W, height=self.menu_height)

        self.content_frame = tk.Frame(self.root, bg=S.COLORS.CONTENT_BG)
        self.content_frame.place(x=0, y=self.menu_height, width=self.W, height=self.H - self.menu_height)

    # ---------- Menu ----------
    def _create_menu(self):
        # Left-aligned button row
        left = tk.Frame(self.menu_frame, bg=S.COLORS.MENU_BG)
        left.place(x=8, rely=0.5, anchor="w")

        self.btn_play = tk.Button(left, text="Play", command=self.show_play_view, **S.MENU_BUTTON)
        self.btn_play.pack(side=tk.LEFT, padx=(0, 8))

        self.btn_tour = tk.Button(left, text="Tournament", command=self.show_tournament_view, **S.MENU_BUTTON)
        self.btn_tour.pack(side=tk.LEFT, padx=(0, 8))

        self.btn_sim = tk.Button(left, text="Simulation", command=self.show_simulation_view, **S.MENU_BUTTON)
        self.btn_sim.pack(side=tk.LEFT, padx=(0, 8))

        # Right-aligned Quit
        right = tk.Frame(self.menu_frame, bg=S.COLORS.MENU_BG)
        right.place(relx=1.0, rely=0.5, anchor="e")
        self.btn_quit = tk.Button(right, text="Quit", command=self.quit, **S.MENU_BUTTON)
        self.btn_quit.pack(side=tk.LEFT, padx=(0, 10))

    # ---------- Content host ----------
    def _create_content(self):
        # nothing inside yet—views will populate this
        pass

    def _unmount_current_view(self):
        if self.current_view is not None:
            # call optional teardown if provided
            if hasattr(self.current_view, "destroy"):
                self.current_view.destroy()
            # and clear the frame
            for w in self.content_frame.winfo_children():
                w.destroy()
            self.current_view = None

    # ---------- View switching ----------
    def show_play_view(self):
        self._unmount_current_view()
        self.current_view = PlayView(
            parent=self.content_frame,
            roster=self.roster,
            human=self.human,
            images_dict=self.images_dict,
            params=self.params
        )
        self.current_view.mount()

    def load_images(self):
        self.images_dict = {}
        self.small_images_dict = {}
        self.mini_images_dict = {}
        for name in self.roster:
            path = f"{self.images_dir}/{name}.png"
            base = tk.PhotoImage(file=path)
            self.images_dict[name] = base
            self.small_images_dict[name] = base.subsample(4, 4)
            self.mini_images_dict[name] = base.subsample(10, 10)

    def show_tournament_view(self):
        self._unmount_current_view()
        self.current_view = TournamentView(
            parent=self.content_frame,
            roster=self.roster,
            small_image_dict=self.small_images_dict,
            params=self.params,
        )
        self.current_view.mount()

    def show_simulation_view(self):
        self._unmount_current_view()
        self.current_view = SimulationView(
            parent=self.content_frame,
            small_images_dict=self.small_images_dict,
            mini_images_dict=self.mini_images_dict,
            params=self.params,

        )
        self.current_view.mount()

    def quit(self):
        self.root.quit()
        self.root.destroy()

    def run(self):
        self.root.mainloop()