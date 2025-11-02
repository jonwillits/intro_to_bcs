import random
from . import players
from .prisoners_dilemma import resolve_round


class EvolutionarySimulation:

    def __init__(self, world_size, params):
        # world_size is (rows, cols)
        self.num_rows, self.num_cols = world_size
        self.params = params

        # generation tracking
        self.generation = 0

        # counters for agent instance naming
        self.init_agent_counter_dict()

        # grid of new agents
        self.grid = []
        self.ai_names_weighted = self.build_weighted_names()
        self.ai_class_by_name = self.build_class_cache()
        self.create_agents_grid()

    def init_agent_counter_dict(self):
        self.agent_counter_dict = {}
        ai_freq_dict = self.params.EvolutionarySimulation.AI_FREQ_DICT
        for name in ai_freq_dict:
            self.agent_counter_dict[name] = 0

    def build_weighted_names(self):
        ai_freq_dict = self.params.EvolutionarySimulation.AI_FREQ_DICT
        names = []
        for name, count in ai_freq_dict.items():
            names.extend([name] * count)
        return names

    def build_class_cache(self):
        """Map string names to classes defined in players.py."""
        ai_freq_dict = self.params.EvolutionarySimulation.AI_FREQ_DICT
        return {name: getattr(players, name) for name in ai_freq_dict.keys()}

    def create_agents_grid(self):
        for r in range(self.num_rows):
            row = []
            for c in range(self.num_cols):
                name = random.choice(self.ai_names_weighted)
                self.agent_counter_dict[name] += 1
                cls = self.ai_class_by_name[name]
                agent = cls(self.params, f"{name}_{self.agent_counter_dict[name]}")
                row.append(agent)
            self.grid.append(row)

    def reset_all_scores(self):
        """Reset every agent's accumulated score before a new generation."""
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                agent = self.grid[i][j]
                if agent is not None:
                    agent.score = 0
                    agent.opponent_score_dict.clear()

    def get_mean_fitness(self):
        """Return average score of all surviving agents."""
        total_score = 0
        count = 0
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                agent = self.grid[i][j]
                if agent is not None:
                    total_score += agent.score
                    count += 1
        return (total_score / count) if count > 0 else 0

    def play_rounds(self, agent1, agent2):
        for _ in range(self.params.EvolutionarySimulation.ROUNDS_PER_TURN):
            agent1_move = agent1.choose_move(agent2.name)
            agent2_move = agent2.choose_move(agent1.name)

            agent1_result, agent2_result = resolve_round(
                agent1_move, agent2_move, self.params.PrisonersDilemma.PAYOFF_MATRIX
            )

            agent1.record_interaction(
                opponent_name=agent2.name,
                my_move=agent1_move,
                their_move=agent2_move,
                my_outcome=agent1_result,
                their_outcome=agent2_result,
            )
            agent2.record_interaction(
                opponent_name=agent1.name,
                my_move=agent2_move,
                their_move=agent1_move,
                my_outcome=agent2_result,
                their_outcome=agent1_result,
            )

    def play_turn(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                agent1 = self.grid[i][j]
                if agent1 is None:
                    continue

                # East
                if j + 1 < self.num_cols:
                    agent2 = self.grid[i][j + 1]
                    if agent2 is not None:
                        self.play_rounds(agent1, agent2)

                # South
                if i + 1 < self.num_rows:
                    agent2 = self.grid[i + 1][j]
                    if agent2 is not None:
                        self.play_rounds(agent1, agent2)

    def select_and_cull(self):
        keep_prop = self.params.EvolutionarySimulation.PROPORTION_TO_KEEP

        cells = []
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                agent = self.grid[i][j]
                if agent is not None:
                    cells.append((i, j, agent))

        if not cells:
            return 0

        random.shuffle(cells)
        cells.sort(key=lambda t: t[2].score, reverse=True)

        total = len(cells)
        keep_n = int(total * keep_prop)
        keep_n = max(1, keep_n)

        # Kill the rest
        for i, j, _ in cells[keep_n:]:
            self.grid[i][j] = None

        return keep_n

    def neighbors4(self, i, j):
        cand = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]
        return [(r, c) for r, c in cand if 0 <= r < self.num_rows and 0 <= c < self.num_cols]

    def spawn_by_name(self, type_name):
        self.agent_counter_dict[type_name] += 1
        cls = self.ai_class_by_name[type_name]
        return cls(self.params, f"{type_name}_{self.agent_counter_dict[type_name]}")

    def reproduce(self):
        """
        Build a new grid from a snapshot of the current grid (synchronous update):
          - If cell is None: copy a random non-None neighbor's type; if none exist, spawn a random type.
          - If cell is occupied: replace with a fresh agent of the same type.
        """
        old = self.grid  # snapshot reference
        next_grid = [[None for _ in range(self.num_cols)] for _ in range(self.num_rows)]

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                current = old[i][j]
                if current is None:
                    # look for any non-empty neighbors in the snapshot
                    neighbor_types = []
                    for (r, c) in self.neighbors4(i, j):
                        agent = old[r][c]
                        if agent is not None:
                            neighbor_types.append(agent.__class__.__name__)

                    if neighbor_types:
                        chosen_type = random.choice(neighbor_types)
                    else:
                        # all neighbors empty → spawn a random type from weighted list
                        chosen_type = random.choice(self.ai_names_weighted)

                    next_grid[i][j] = self.spawn_by_name(chosen_type)

                else:
                    # occupied → clone same type (new individual)
                    type_name = current.__class__.__name__
                    next_grid[i][j] = self.spawn_by_name(type_name)

        # commit synchronously
        self.grid = next_grid

    def get_population_frequencies(self):
        freq_dict = {name: 0 for name in self.params.EvolutionarySimulation.AI_FREQ_DICT.keys()}

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                agent = self.grid[i][j]
                if agent is not None:
                    t = agent.__class__.__name__
                    freq_dict.setdefault(t, 0)
                    freq_dict[t] += 1

        return freq_dict

    def run_simulation_step(self):
        # play PD everywhere
        self.play_turn()

        # cull losers
        self.select_and_cull()

        # reproduce into empty and existing cells
        self.reproduce()

        # increment generation
        self.generation += 1

        # reset scores for next generation
        self.reset_all_scores()