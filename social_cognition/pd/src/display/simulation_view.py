# src/simulation_view.py
import tkinter as tk
from . import display_styles as S
from .tooltips import attach_tooltip
from ..evolutionary_simulation import EvolutionarySimulation

class SimulationView:
    def __init__(self, parent, small_images_dict, mini_images_dict, params):
        self.parent = parent
        self.params = params
        self.info_frame = None
        self.world_frame = None
        self.world_frame_padding = 20
        self.grid_frame = None
        self.grid_rows = None
        self.grid_cols = None
        self.mini_image_size = 20
        self.mini_images_dict = mini_images_dict
        self.small_images_dict = small_images_dict
        self.simulation = None
        self.ui_frame = None
        self.is_running = False
        self.step_phase = "compete"  # cycles: compete -> select -> reproduce -> compete
        self.phase_button = None
        self.run_button = None
        self.take_turn_button = None
        self.reset_button = None
        self.step_button = None
        self.rounds_entry = None
        self.keep_entry = None
        self.noise_entry = None
        self.grid_labels = []
        self.key_frame = None
        self.key_count_labels = {}

        self.ai_colors = {
            'NiceAI': 'green',
            'MeanAI': 'red',
            'RandomAI': 'yellow',
            'TitForTatAI': 'blue',
            'WinStayLoseShiftAI': 'orange'
        }

        self._defaults = {
            "ROUNDS_PER_TURN": self.params.EvolutionarySimulation.ROUNDS_PER_TURN,
            "PROPORTION_TO_KEEP": self.params.EvolutionarySimulation.PROPORTION_TO_KEEP,
            # AI noise may live at params.AI.NOISE (or .noise in your classes earlier);
            # we’ll read both and prefer NOISE if present.
            "AI_NOISE": getattr(self.params.AI, "NOISE", getattr(self.params.AI, "noise", 0.0)),
        }

    def mount(self):
        # left quarter


        # right three-quarters
        self.world_frame = tk.Frame(self.parent, bg="grey")
        self.world_frame.place(relx=0.25, rely=0.0, relwidth=0.75, relheight=1.0, anchor="nw")

        self.create_world_grid()
        self.parent.update_idletasks()
        self.populate_world_grid()

        self.info_frame = tk.Frame(self.parent, bg=S.COLORS.CONTENT_BG)
        self.info_frame.place(relx=0.0, rely=0.0, relwidth=0.25, relheight=1.0, anchor="nw")
        self.create_key_panel()
        self.create_ui_panel()

        self.create_tool_tips()

    def create_tool_tips(self):
        attach_tooltip(self.run_button, "play.run")
        attach_tooltip(self.phase_button, "play.phase")
        attach_tooltip(self.take_turn_button, "play.take_turn")  # if you have the full-generation button
        attach_tooltip(self.reset_button, "play.reset")

        attach_tooltip(self.rounds_entry, "sim.rounds")
        attach_tooltip(self.keep_entry, "sim.keep")
        attach_tooltip(self.noise_entry, "sim.noise")

        attach_tooltip(self.key_frame, "legend.panel")
        # (optional) for the grid as a whole:
        attach_tooltip(self.grid_frame, "grid.cell")

    def create_ui_panel(self):
        # Takes the remaining 70% height of info_frame, below the key panel
        self.ui_frame = tk.Frame(self.info_frame, bg=S.COLORS.CONTENT_BG)
        self.ui_frame.place(x=0, rely=0.3, relwidth=1.0, relheight=0.7, anchor="nw")

        # Step button
        self.take_turn_button = tk.Button(
            self.ui_frame,
            text="Take Turn",
            command=self.on_take_turn,
            **S.CONTENT_BUTTON
        )
        self.take_turn_button.place(relx=0.5, rely=0.7, width=110, height=32, anchor="center")

        # Run / Pause button
        self.run_button = tk.Button(
            self.ui_frame,
            text="Run",
            command=self.on_run_pause,
            **S.CONTENT_BUTTON
        )
        self.run_button.place(relx=0.5, rely=0.8, width=110, height=32, anchor="center")

        self.reset_button = tk.Button(
            self.ui_frame,
            text="Reset",
            command=self.on_reset,
            **S.CONTENT_BUTTON
        )
        self.reset_button.place(relx=0.5, rely=0.9, width=110, height=32, anchor="center")

        # Phase Step button (cycles Compete -> Selection -> Reproduce)
        self.phase_button = tk.Button(
            self.ui_frame,
            text="Compete",
            command=self.on_phase_step,
            **S.CONTENT_BUTTON
        )
        # adjust placement as you like
        self.phase_button.place(relx=0.50, rely=0.6, width=110, height=32, anchor="center")

        tk.Label(self.ui_frame, text="Simulation Parameters", **S.CONTENT_TEXT).place(relx=0.5, rely=0.1, anchor="center")

        # --- Rounds per Turn ---
        tk.Label(self.ui_frame, text="Rounds per Turn", **S.CONTENT_TEXT) \
            .place(relx=0.65, rely=0.2, anchor="e")
        self.rounds_entry = tk.Entry(self.ui_frame, width=5)
        self.rounds_entry.insert(0, str(self.params.EvolutionarySimulation.ROUNDS_PER_TURN))
        self.rounds_entry.place(relx=0.70, rely=0.2, width=40, anchor="w")

        # --- Proportion to Keep ---
        tk.Label(self.ui_frame, text="Proportion to Keep", **S.CONTENT_TEXT) \
            .place(relx=0.65, rely=0.3, anchor="e")
        self.keep_entry = tk.Entry(self.ui_frame, width=5)
        self.keep_entry.insert(0, str(self.params.EvolutionarySimulation.PROPORTION_TO_KEEP))
        self.keep_entry.place(relx=0.70, rely=0.3, width=40, anchor="w")

        # --- AI Noise ---
        tk.Label(self.ui_frame, text="AI Noise", **S.CONTENT_TEXT) \
            .place(relx=0.65, rely=0.4, anchor="e")
        self.noise_entry = tk.Entry(self.ui_frame, width=5)
        # prefer NOISE if present
        _curr_noise = getattr(self.params.AI, "NOISE", getattr(self.params.AI, "noise", 0.0))
        self.noise_entry.insert(0, str(_curr_noise))
        self.noise_entry.place(relx=0.70, rely=0.4, width=40, anchor="w")

    def on_take_turn(self):
        # Guard: simulation must exist and labels must be created
        if not self.simulation or not self.grid_labels:
            return
        self.update_params_from_ui()
        self.simulation.run_simulation_step()
        self.update_agent_labels()
        self.update_key_counts()
        self.title_lbl.config(text=f"Summary (Generation: {self.simulation.generation})")

    def on_run_pause(self):
        if not self.is_running:
            # Start running
            self.is_running = True
            self.run_button.config(text="Pause")
            self.run_loop()
        else:
            # Pause
            self.is_running = False
            self.run_button.config(text="Run")

    def run_loop(self):
        if not self.is_running:
            return  # stop looping
        self.update_params_from_ui()
        self.on_take_turn()  # run one generation
        self.parent.after(50, self.run_loop)  # schedule next cycle (50ms)

    def on_phase_step(self):
        if not self.simulation or not self.grid_labels:
            return
        self.update_params_from_ui()

        if self.step_phase == "compete":
            # 1) Interactions only
            self.simulation.play_turn()
            self.update_agent_labels()
            self.update_key_counts()

            self.step_phase = "select"
            self.phase_button.config(text="Selection")

        elif self.step_phase == "select":
            # 2) Cull losers (set some cells to None)
            self.simulation.select_and_cull()
            self.update_agent_labels()  # will paint None cells white
            self.update_key_counts()

            self.step_phase = "reproduce"
            self.phase_button.config(text="Reproduce")

        else:  # "reproduce"
            # 3) Fill Nones and clone survivors
            self.simulation.reproduce()

            # Keep semantics consistent with your one-shot generation:
            # increment generation and reset scores at generation boundary
            self.simulation.generation += 1
            self.simulation.reset_all_scores()

            self.update_agent_labels()
            self.update_key_counts()

            self.step_phase = "compete"
            self.phase_button.config(text="Compete")
            self.title_lbl.config(text=f"Summary (Generation: {self.simulation.generation})")

    def on_reset(self):
        if self.grid_rows is None or self.grid_cols is None:
            return

        # restore defaults in params
        self.params.EvolutionarySimulation.ROUNDS_PER_TURN = self._defaults["ROUNDS_PER_TURN"]
        self.params.EvolutionarySimulation.PROPORTION_TO_KEEP = self._defaults["PROPORTION_TO_KEEP"]
        if hasattr(self.params.AI, "NOISE"):
            self.params.AI.NOISE = self._defaults["AI_NOISE"]

        # reset entry boxes
        self.rounds_entry.delete(0, "end")
        self.rounds_entry.insert(0, str(self._defaults["ROUNDS_PER_TURN"]))

        self.keep_entry.delete(0, "end")
        self.keep_entry.insert(0, str(self._defaults["PROPORTION_TO_KEEP"]))

        self.noise_entry.delete(0, "end")
        self.noise_entry.insert(0, str(self._defaults["AI_NOISE"]))

        # create fresh simulation (new random world, generation=0)
        self.simulation = EvolutionarySimulation((self.grid_rows, self.grid_cols), self.params)

        # refresh visuals
        self.update_agent_labels()
        self.update_key_counts()

        # also reset the phase button state if you like
        self.step_phase = "compete"
        if self.phase_button:
            self.phase_button.config(text="Compete")

        self.title_lbl.config(text=f"Summary (Generation: {self.simulation.generation})")

    def create_key_panel(self):

        # Takes full width, top 30% height of info_frame
        self.key_frame = tk.Frame(self.info_frame, bg=S.COLORS.CONTENT_BG)
        self.key_frame.place(x=0, y=0, relwidth=1.0, relheight=0.3, anchor="nw")

        # ----- New: Section Title -----
        self.title_lbl = tk.Label(
            self.key_frame,
            text=f"Summary (Generation: {self.simulation.generation})",
            **S.CONTENT_TEXT
        )
        # place near top, centered horizontally
        self.title_lbl.place(relx=0.5, rely=0.02, anchor="n")

        # ----- Rows of AI entries -----
        rows = list(self.ai_colors.items())
        row_h_rel = 0.85 / max(1, len(rows))  # reserve ~15% height for header

        for idx, (tname, color) in enumerate(rows):
            rely = 0.12 + idx * row_h_rel  # shift down a bit to make room

            # color box
            box = tk.Label(self.key_frame, bg=color, bd=1, relief="solid")
            box.place(relx=0.02, rely=rely + 0.15 * row_h_rel,
                      width=16, height=16, anchor="nw")

            # AI name
            name_lbl = tk.Label(self.key_frame, text=tname, **S.CONTENT_TEXT)
            name_lbl.place(relx=0.08, rely=rely + 0.1 * row_h_rel, anchor="nw")

            # population count (right aligned)
            cnt_lbl = tk.Label(self.key_frame, text="0", **S.CONTENT_TEXT)
            cnt_lbl.place(relx=1.0, x=-10, rely=rely + 0.1 * row_h_rel, anchor="ne")

            self.key_count_labels[tname] = cnt_lbl

    def update_params_from_ui(self):
        """Read entries, update params, and push AI noise to existing agents."""
        # Rounds per Turn (int)
        try:
            rpt = int(self.rounds_entry.get())
            if rpt >= 0:
                self.params.EvolutionarySimulation.ROUNDS_PER_TURN = rpt
        except Exception:
            pass  # keep old value

        # Proportion to Keep (float in [0,1])
        try:
            keep = float(self.keep_entry.get())
            # light clamping, very simple
            keep = 0.0 if keep < 0 else (1.0 if keep > 1.0 else keep)
            self.params.EvolutionarySimulation.PROPORTION_TO_KEEP = keep
        except Exception:
            pass

        # AI Noise (float in [0,1]), set on params and all current agents
        try:
            nz = float(self.noise_entry.get())
            nz = 0.0 if nz < 0 else (1.0 if nz > 1.0 else nz)
            # set both attributes to be friendly with earlier code paths
            if hasattr(self.params.AI, "NOISE"):
                self.params.AI.NOISE = nz
            if hasattr(self.params.AI, "noise"):
                self.params.AI.noise = nz

            # update all existing agents immediately
            if self.simulation:
                for r in range(self.grid_rows):
                    for c in range(self.grid_cols):
                        a = self.simulation.grid[r][c]
                        if a is not None and hasattr(a, "noise"):
                            a.noise = nz
        except Exception:
            pass

    def update_key_counts(self):
        if not self.simulation:
            return
        freq = self.simulation.get_population_frequencies()
        for tname, lbl in self.key_count_labels.items():
            lbl.config(text=str(freq.get(tname, 0)))

    def populate_world_grid(self):
        if self.grid_rows is None or self.grid_cols is None:
            self.parent.after(10, self.populate_world_grid)
            return

        self.simulation = EvolutionarySimulation((self.grid_rows, self.grid_cols), self.params)
        self.update_key_counts()

        # Create text labels ONCE after grid created
        if not self.grid_labels:
            self.create_agent_labels()

        self.update_agent_labels()

    def create_world_grid(self):
        self.world_frame.update_idletasks()

        w = self.world_frame.winfo_width() - self.world_frame_padding
        h = self.world_frame.winfo_height() - self.world_frame_padding

        # number of 20px cells that fit
        self.grid_cols = w // self.mini_image_size
        self.grid_rows = h // self.mini_image_size

        # pixel size of grid based on whole cell counts
        gw = self.grid_cols * self.mini_image_size
        gh = self.grid_rows * self.mini_image_size

        # NEW: if grid already exists, just move/resize it
        if self.grid_frame is None:
            self.grid_frame = tk.Frame(self.world_frame, bg=S.COLORS.CONTENT_BG)

        self.grid_frame.place(
            x=(w - gw)//2 + self.world_frame_padding//2,
            y=(h - gh)//2 + self.world_frame_padding//2,
            width=gw,
            height=gh
        )

        print(f"Grid cells: {self.grid_cols} x {self.grid_rows}")
        print(f"Pixel grid: {gw} x {gh}")

        if not self.grid_labels:
            self.create_agent_labels()

    def create_agent_labels(self):
        self.grid_labels = []
        for r in range(self.grid_rows):
            row = []
            for c in range(self.grid_cols):
                lbl = tk.Label(
                    self.grid_frame,
                    width=2, height=1,  # enough to show score
                    bg="gray",
                    fg="black",
                    text="0",  # start score
                    font=("Arial", 8)
                )
                lbl.place(
                    x=c * self.mini_image_size,
                    y=r * self.mini_image_size,
                    width=self.mini_image_size,
                    height=self.mini_image_size
                )
                row.append(lbl)
            self.grid_labels.append(row)

    def update_agent_labels(self):
        sim = self.simulation
        for r in range(self.grid_rows):
            for c in range(self.grid_cols):
                agent = sim.grid[r][c]
                lbl = self.grid_labels[r][c]

                if agent is None:
                    lbl.config(bg="black", text="")
                    continue

                type_name = agent.__class__.__name__
                color = self.ai_colors[type_name]

                if agent.score is not None and agent.score is not 0:
                    score_text = agent.score
                else:
                    score_text = ""

                lbl.config(
                    bg=color,
                    text=str(score_text)
                )



    def destroy(self):
        pass