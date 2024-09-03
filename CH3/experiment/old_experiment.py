import numpy as np
from scipy import stats as scs
import tkinter as tk
import math

class Display:

    def __init__(self, the_experiment):
        self.the_experiment = the_experiment

        self.root = tk.Tk()
        self.root.title("Experiment Replication Simulation")

        self.window_height = 850
        self.option_frame_width = 250
        self.results_frame_width = 1300

        self.distribution_plot_width = 750
        self.distribution_plot_height = 200

        self.init_option_frame()
        self.init_results_frame()
        self.update_results_canvas()


    def init_option_frame(self):

        self.option_frame = tk.Frame(self.root, height=self.window_height, width=self.option_frame_width, bg='black')
        self.option_frame.pack(side=tk.LEFT)

        self.run_experiment_button = tk.Button(self.option_frame, text="Run Experiment", fg="black", command=self.clicked_run_experiment, width=10,
                                     padx=20, pady=20)
        self.run_experiment_button.place(x=25, y=25)

        self.option_label_list = []
        self.option_dict = {}

        self.option_label_list.append(tk.Label(self.option_frame, text="Population", fg="white", bg="black"))
        self.option_label_list.append(tk.Label(self.option_frame, text="Mean", fg="white", bg="black"))
        self.option_label_list.append(tk.Label(self.option_frame, text="StDev", fg="white", bg="black"))

        self.option_label_list.append(tk.Label(self.option_frame, text="Experimental Group Effect Size", fg="white", bg="black"))
        self.option_label_list.append(tk.Label(self.option_frame, text="Mean", fg="white", bg="black"))
        self.option_label_list.append(tk.Label(self.option_frame, text="StDev", fg="white", bg="black"))

        self.option_label_list.append(tk.Label(self.option_frame, text="Control Group Effect Size", fg="white", bg="black"))
        self.option_label_list.append(tk.Label(self.option_frame, text="Mean", fg="white", bg="black"))
        self.option_label_list.append(tk.Label(self.option_frame, text="StDev", fg="white", bg="black"))

        self.option_label_list.append(tk.Label(self.option_frame, text="Sample Size", fg="white", bg="black"))

        self.option_label_list[0].place(x=25, y=125)
        self.option_label_list[1].place(x=75, y=150)
        self.option_label_list[2].place(x=75, y=185)

        self.option_label_list[3].place(x=25, y=250)
        self.option_label_list[4].place(x=75, y=275)
        self.option_label_list[5].place(x=75, y=310)

        self.option_label_list[6].place(x=25, y=375)
        self.option_label_list[7].place(x=75, y=400)
        self.option_label_list[8].place(x=75, y=435)

        self.option_label_list[9].place(x=25, y=500)

        self.option_dict[self.option_label_list[1]] = tk.Entry(self.option_frame, bd=1, width=5)
        self.option_dict[self.option_label_list[1]].place(x=125, y=150)
        self.option_dict[self.option_label_list[2]] = tk.Entry(self.option_frame, bd=1, width=5)
        self.option_dict[self.option_label_list[2]].place(x=125, y=185)
        self.option_dict[self.option_label_list[4]] = tk.Entry(self.option_frame, bd=1, width=5)
        self.option_dict[self.option_label_list[4]].place(x=125, y=275)
        self.option_dict[self.option_label_list[5]] = tk.Entry(self.option_frame, bd=1, width=5)
        self.option_dict[self.option_label_list[5]].place(x=125, y=310)
        self.option_dict[self.option_label_list[7]] = tk.Entry(self.option_frame, bd=1, width=5)
        self.option_dict[self.option_label_list[7]].place(x=125, y=400)
        self.option_dict[self.option_label_list[8]] = tk.Entry(self.option_frame, bd=1, width=5)
        self.option_dict[self.option_label_list[8]].place(x=125, y=435)
        self.option_dict[self.option_label_list[9]] = tk.Entry(self.option_frame, bd=1, width=5)
        self.option_dict[self.option_label_list[9]].place(x=125, y=500)

        self.option_dict[self.option_label_list[1]].insert(tk.END, str(self.the_experiment.pop_mean))
        self.option_dict[self.option_label_list[2]].insert(tk.END, str(self.the_experiment.pop_stdev))
        self.option_dict[self.option_label_list[4]].insert(tk.END, str(self.the_experiment.e_pop_effect_mean))
        self.option_dict[self.option_label_list[5]].insert(tk.END, str(self.the_experiment.e_pop_effect_stdev))
        self.option_dict[self.option_label_list[7]].insert(tk.END, str(self.the_experiment.c_pop_effect_mean))
        self.option_dict[self.option_label_list[8]].insert(tk.END, str(self.the_experiment.c_pop_effect_stdev))
        self.option_dict[self.option_label_list[9]].insert(tk.END, str(self.the_experiment.sample_size))

        self.reset_button = tk.Button(self.option_frame, text="Reset History", fg="black", command=self.clicked_reset_history_button, width=6,
                                     padx=10, pady=10)
        self.reset_button.place(x=25, y=625)


    def init_results_frame(self):
        self.results_frame = tk.Frame(self.root, height=self.window_height, width=self.results_frame_width, bg='black')
        self.results_frame.pack(side=tk.LEFT)
        self.results_canvas = tk.Canvas(self.results_frame, height=self.window_height, width=self.results_frame_width, bg="black")
        self.results_canvas.pack(side=tk.LEFT)


    def clicked_reset_history_button(self):
        self.the_experiment = Experiment()
        self.update_results_canvas()


    def clicked_run_experiment(self):
        pop_mean = float(self.option_dict[self.option_label_list[1]].get())
        pop_stdev = float(self.option_dict[self.option_label_list[2]].get())
        e_pop_effect_mean = float(self.option_dict[self.option_label_list[4]].get())
        e_pop_effect_stdev = float(self.option_dict[self.option_label_list[5]].get())
        c_pop_effect_mean = float(self.option_dict[self.option_label_list[7]].get())
        c_pop_effect_stdev = float(self.option_dict[self.option_label_list[8]].get())
        sample_size = int(self.option_dict[self.option_label_list[9]].get())

        self.the_experiment.run_experiment(pop_mean, pop_stdev, e_pop_effect_mean, e_pop_effect_stdev, c_pop_effect_mean, c_pop_effect_stdev, sample_size)
        self.update_results_canvas()


    def display_scatter_plot(self, x, y, g1_scores, g2_scores, g1_label, g2_label, main_label, y_max, y_min, color1, color2):

        self.results_canvas.create_text(x+100, y+25, font="Times 20", text=main_label, fill="white")
        self.results_canvas.create_text(x+60, y+260, font="Times 16", text=g1_label, fill="white")
        self.results_canvas.create_text(x+150, y+260, font="Times 16", text=g2_label, fill="white")

        self.results_canvas.create_line(x, y+35, x, y+235, fill="white", width=5)
        self.results_canvas.create_line(x+200, y+235, x-3, y+235, fill="white", width=5)

        quartile_score = (y_max - y_min)/4
        y_axis_labels = np.array([y_min, np.round(y_min+quartile_score).astype(int), np.round(y_min+2*quartile_score).astype(int), np.round(y_min+3*quartile_score).astype(int), y_max])
        for i in range(5):
            if quartile_score > 1:
                self.results_canvas.create_text(x-15, y-i*48+232, font="Times 12", text="{:0.0f}".format(y_axis_labels[i]), fill="white")
            else:
                self.results_canvas.create_text(x-15, y-i*48+232, font="Times 12", text="{:0.2f}".format(y_axis_labels[i]), fill="white")

        circle_size = 10

        score_range = y_max - y_min
        y_pixel_range = 195
        pixels_per_score = y_pixel_range / score_range

        if g1_scores is not None:
            for i in range(len(g1_scores)):
                rand_scatter = np.random.randint(-5,5)
                score1 = g1_scores[i]
                score2 = g2_scores[i]

                score1_ypos = y+225 - (score1-y_min)*pixels_per_score
                score2_ypos = y+225 - (score2-y_min)*pixels_per_score

                self.results_canvas.create_oval(x+60+rand_scatter, score1_ypos, x+60+circle_size+rand_scatter, score1_ypos+circle_size, fill=color1)
                self.results_canvas.create_oval(x+150+rand_scatter, score2_ypos, x+150+circle_size+rand_scatter, score2_ypos+circle_size, fill=color2)


    def show_distribution_axes(self, x_start, y_start, x_range, min_x):

        num_ticks = 20

        tick_interval_pixels = self.distribution_plot_width / num_ticks
        tick_interval_units = x_range / num_ticks

        self.results_canvas.create_line(x_start, y_start, x_start+self.distribution_plot_width, y_start, fill="white", width=5)
        self.results_canvas.create_line(x_start, y_start+2, x_start, y_start-self.distribution_plot_height, fill="white", width=5)
        self.results_canvas.create_text(x_start-12, y_start-self.distribution_plot_height/2, font="Times 16", text="P", fill="white")

        x_label = min_x
        for i in range(num_ticks+1):
            self.results_canvas.create_text(x_start+i*tick_interval_pixels, y_start+15, font="Times 12", text="{:0.1f}".format(x_label), fill="white")
            x_label += tick_interval_units
            x1_coord = x_start+i*tick_interval_pixels
            self.results_canvas.create_line(x1_coord, y_start, x1_coord, y_start-10, fill="white", width=3)


    def show_distributions(self, x_start, y_start, pop_mean1, pop_mean2, pop_stdev1, pop_stdev2, x_range, min_x, color1, color2, y_max, label1, label2):

        num_pts = 100
        x_pixels_per_pt = self.distribution_plot_width / num_pts
        x_units_per_pt = x_range / num_pts
        y_pixels_per_unit = self.distribution_plot_height / y_max

        coordinate_list1 = []
        coordinate_list2 = []
        x_value = min_x

        for i in range(num_pts+1):
            x_coord = x_start+i*(x_pixels_per_pt)
            y1_value = (1.0 / (pop_stdev1 * math.sqrt(2*math.pi))) * math.exp(-0.5*((x_value - pop_mean1) / pop_stdev1) ** 2)
            y2_value = (1.0 / (pop_stdev2 * math.sqrt(2*math.pi))) * math.exp(-0.5*((x_value - pop_mean2) / pop_stdev2) ** 2)
            y1_coord = y_start - y1_value*y_pixels_per_unit
            y2_coord = y_start - y2_value*y_pixels_per_unit
            coordinate_list1.append(x_coord)
            coordinate_list1.append(y1_coord)
            coordinate_list2.append(x_coord)
            coordinate_list2.append(y2_coord)
            x_value += x_units_per_pt
        coordinate_list1 += coordinate_list1[:2]
        coordinate_list2 += coordinate_list2[:2]
        self.results_canvas.create_polygon(coordinate_list1, fill=color1, outline="white")
        self.results_canvas.create_polygon(coordinate_list2, fill=color2, outline="white")

        for i in range(0, len(coordinate_list1)-2, 2):
            x1_coord = coordinate_list1[i]
            y1_coord = coordinate_list1[i+1]
            x2_coord = coordinate_list2[i]
            y2_coord = coordinate_list2[i+1]
            self.results_canvas.create_oval(x1_coord-2, y1_coord-2, x1_coord+2, y1_coord+2, fill=color1)
            self.results_canvas.create_oval(x2_coord-2, y2_coord-2, x2_coord+2, y2_coord+2, fill=color2)

        self.results_canvas.create_rectangle(x_start+10, y_start-self.distribution_plot_height+30, x_start+30, y_start-self.distribution_plot_height+10, fill=color1)
        self.results_canvas.create_rectangle(x_start+10, y_start-self.distribution_plot_height+40, x_start+30, y_start-self.distribution_plot_height+60, fill=color2)
        self.results_canvas.create_text(x_start+90, y_start-self.distribution_plot_height+20, font="Times 16", text="{:<20}".format(label1), fill="white")
        self.results_canvas.create_text(x_start+90, y_start-self.distribution_plot_height+50, font="Times 16", text="{:<20}".format(label2), fill="white")


    def show_distribution_mean(self, sample_mean, x_start, y_start, x_range, x_min, y_max, pop_mean, pop_stdev, color):

        x_pixels_per_unit = self.distribution_plot_width / x_range
        y_pixels_per_unit = self.distribution_plot_height / y_max

        x = x_start + (sample_mean-x_min)*x_pixels_per_unit
        y = y_pixels_per_unit * (1.0 / (pop_stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((sample_mean - pop_mean) / pop_stdev) ** 2)

        self.results_canvas.create_line(x, y_start, x, y_start-y, fill=color, width=5)


    def display_distribution_plot(self, x_start, y_start, pop_mean1, pop_stdev1, fill_color1, mean_color1, label1, pop_mean2, pop_stdev2, fill_color2, mean_color2, label2, title, sample1_mean, sample2_mean):

        e_min_x = int(round(pop_mean1 - 5 * pop_stdev1))
        e_max_x = int(round(pop_mean1 + 5 * pop_stdev1))
        c_min_x = int(round(pop_mean2 - 5 * pop_stdev2))
        c_max_x = int(round(pop_mean2 + 5 * pop_stdev2))
        max_x = np.max(np.array([e_max_x,c_max_x]))
        min_x = np.min(np.array([e_min_x,c_min_x]))
        x_range = max_x - min_x

        y_max = np.max(np.array([(1.0 / (pop_stdev1 * math.sqrt(2*math.pi))), (1.0 / (pop_stdev2 * math.sqrt(2*math.pi)))]))

        self.results_canvas.create_text(x_start+125, y_start-self.distribution_plot_height-10, font="Times 24", text=title, fill="white")
        self.show_distribution_axes(x_start, y_start, x_range, min_x)
        self.show_distributions(x_start, y_start, pop_mean1, pop_mean2, pop_stdev1, pop_stdev2, x_range, min_x, fill_color1, fill_color2, y_max, label1, label2)
        if sample1_mean is not None:
            self.show_distribution_mean(sample1_mean, x_start, y_start, x_range, min_x, y_max, pop_mean1, pop_stdev1, mean_color1)
        if sample2_mean is not None:
            self.show_distribution_mean(sample2_mean, x_start, y_start, x_range, min_x, y_max, pop_mean2, pop_stdev2, mean_color2)

    def display_history(self, x, y):
        self.results_canvas.create_text(x, y, font="Times 24", text="History", fill="white")
        header_string1 = "                   Exp. Group Imp.           Control Group Imp.                       "
        header_string2 = "Exp.#     n        Mean     StDev            Mean      StDev             t           p"
        self.results_canvas.create_text(x+200, y+25, font="Times 16", text=header_string1, fill="white")
        self.results_canvas.create_text(x+190, y+45, font="Times 16", text=header_string2, fill="white")
        for i in range(len(self.the_experiment.history_dict_list)):

            history_dict = self.the_experiment.history_dict_list[i]

            if history_dict['p'] < 0.0005:
                p = "<0.001"
            else:
                p = "{:0.3f} ".format(history_dict['p'])

            result_string = "{:>2}       {}        {:0.2f}       {:0.2f}                {:0.2f}       {:0.2f}            {:0.2f}      {:>6}".format(i+1,
                                                                                                                                                         history_dict['sample_size'],
                                                                                                                                                         history_dict['e_sample_effect_mean'],
                                                                                                                                                         history_dict['e_sample_effect_stdev'],
                                                                                                                                                         history_dict['c_sample_effect_mean'],
                                                                                                                                                         history_dict['c_sample_effect_stdev'],
                                                                                                                                                         history_dict['t'],
                                                                                                                                                         p)

            result_string_len_offset = int(round(len(result_string)/2))
            self.results_canvas.create_text(x+165+result_string_len_offset, y+70+i*18, font="Times 14", text=result_string, fill="white")


    def update_results_canvas(self):
        self.results_canvas.delete("all")

        self.results_canvas.create_text(75, 25, font="Times 24", text="Raw Scores", fill="white")


        color1 = "#0000FF"
        color2 = "#FFA500"
        color3 = "#333333"
        color4 = "#DDDDDD"
        color5 = "#0000B1"
        color6 = "#B17200"
        color7 = "#666666"
        color8 = "#000000"

        if len(self.the_experiment.history_dict_list) == 0:
            max_score = self.the_experiment.max_score
            min_score = self.the_experiment.min_score
            max_improvement = self.the_experiment.max_improvement
            min_improvement = self.the_experiment.min_improvement
        else:
            max_score = self.the_experiment.history_dict_list[-1]['max_score']
            min_score = self.the_experiment.history_dict_list[-1]['min_score']
            max_improvement = self.the_experiment.history_dict_list[-1]['max_improvement']
            min_improvement = self.the_experiment.history_dict_list[-1]['min_improvement']

        self.display_scatter_plot(75, 30,
                         self.the_experiment.e_sample_start, self.the_experiment.e_sample_final,
                         "Starting\nScores", "Final\nScores", "Experimental Group",
                         max_score, min_score, color4, color1)

        self.display_scatter_plot(325, 30,
                         self.the_experiment.c_sample_start, self.the_experiment.c_sample_final,
                         "Starting\nScores", "Final\nScores", "Control Group",
                         max_score, min_score, color4, color2)

        self.display_scatter_plot(575, 30,
                         self.the_experiment.e_sample_effect, self.the_experiment.c_sample_effect,
                         "Experimental\nGroup", "Control\nGroup", "Improvement",
                         max_improvement, min_improvement, color1, color2)

        if len(self.the_experiment.history_dict_list) > 0:
            e_mean = self.the_experiment.e_sample_effect.mean()
            c_mean = self.the_experiment.c_sample_effect.mean()
            d_mean = e_mean-c_mean
        else:
            e_mean = None
            c_mean = None
            d_mean = None

        self.display_distribution_plot(25, 550,
                                       self.the_experiment.simulation_results['sim_e_effect_mean'], self.the_experiment.simulation_results['sim_e_effect_stdev'], color1, color5, "Exp. Group",
                                       self.the_experiment.simulation_results['sim_c_effect_mean'], self.the_experiment.simulation_results['sim_c_effect_stdev'], color2, color6, "Con. Group",
                                       "Improvement           ", e_mean, c_mean)

        self.display_distribution_plot(25, 550+self.distribution_plot_height+75,
                                       0, self.the_experiment.simulation_results['sim_ec_diff_stdev'], color3, color7, "H0",
                                       self.the_experiment.simulation_results['sim_ec_diff_mean'], self.the_experiment.simulation_results['sim_ec_diff_stdev'], color4, color8, "H1",
                                       "Improvement Difference", d_mean, None)



        self.display_history(825, 25)


        self.root.update()




class Experiment:

    def __init__(self):

        self.pop_mean = 100
        self.pop_stdev = 10

        self.e_pop_effect_mean = 2
        self.e_pop_effect_stdev = 10

        self.c_pop_effect_mean = 0
        self.c_pop_effect_stdev = 10

        self.sample_size = 20

        self.max_score = 100
        self.min_score = 0

        self.max_improvement = 20
        self.min_improvement = 0

        self.history_dict_list = []

        self.e_sample_start = None
        self.e_sample_effect = None
        self.e_sample_final = None
        self.c_sample_start = None
        self.c_sample_effect = None
        self.c_sample_final = None

        self.simulation_results = self.simulate_scores()


    def run_experiment(self, pop_mean, pop_stdev, e_pop_effect_mean, e_pop_effect_stdev, c_pop_effect_mean, c_pop_effect_stdev, sample_size):
        self.pop_mean = pop_mean
        self.pop_stdev = pop_stdev
        self.e_pop_effect_mean = e_pop_effect_mean
        self.e_pop_effect_stdev = e_pop_effect_stdev
        self.c_pop_effect_mean = c_pop_effect_mean
        self.c_pop_effect_stdev = c_pop_effect_stdev
        self.sample_size = sample_size

        self.e_sample_start, self.e_sample_effect, self.e_sample_final, self.c_sample_start, self.c_sample_effect, self.c_sample_final = self.gather_sample()
        result_dict = self.summarize_scores(self.e_sample_start, self.e_sample_effect, self.e_sample_final, self.c_sample_start, self.c_sample_effect, self.c_sample_final)
        self.history_dict_list.append(result_dict)

        self.simulation_results = self.simulate_scores()


    def simulate_scores(self):
        n = 20000
        e_sample_start_matrix = np.zeros([n, self.sample_size])
        c_sample_start_matrix = np.zeros([n, self.sample_size])
        e_sample_effect_matrix = np.zeros([n, self.sample_size])
        c_sample_effect_matrix = np.zeros([n, self.sample_size])
        e_sample_final_matrix = np.zeros([n, self.sample_size])
        c_sample_final_matrix = np.zeros([n, self.sample_size])

        for i in range(n):
            e_sample_start, e_sample_effect, e_sample_final, c_sample_start, c_sample_effect, c_sample_final = self.gather_sample()
            e_sample_start_matrix[i,:] = e_sample_start
            c_sample_start_matrix[i,:] = c_sample_start
            e_sample_effect_matrix[i,:] = e_sample_effect
            c_sample_effect_matrix[i,:] = c_sample_effect
            e_sample_final_matrix[i,:] = e_sample_final
            c_sample_final_matrix[i,:] = c_sample_final

        simulation_results_dict = {}

        simulation_results_dict['n'] = n

        essm = e_sample_start_matrix.mean(1)
        esem = e_sample_effect_matrix.mean(1)
        esfm = e_sample_final_matrix.mean(1)

        cssm = c_sample_start_matrix.mean(1)
        csem = c_sample_effect_matrix.mean(1)
        csfm = c_sample_final_matrix.mean(1)

        group_mean_differences = esem - csem

        simulation_results_dict['sim_ec_diff_mean'] = group_mean_differences.mean()
        simulation_results_dict['sim_ec_diff_stdev'] = group_mean_differences.std()

        simulation_results_dict['sim_e_start_mean'] = essm.mean()
        simulation_results_dict['sim_e_start_stdev'] = essm.std()
        simulation_results_dict['sim_e_effect_mean'] = esem.mean()
        simulation_results_dict['sim_e_effect_stdev'] = esem.std()
        simulation_results_dict['sim_e_final_mean'] = esfm.mean()
        simulation_results_dict['sim_e_final_stdev'] = esfm.std()

        simulation_results_dict['sim_c_start_mean'] = cssm.mean()
        simulation_results_dict['sim_c_start_stdev'] = cssm.std()
        simulation_results_dict['sim_c_effect_mean'] = csem.mean()
        simulation_results_dict['sim_c_effect_stdev'] = csem.std()
        simulation_results_dict['sim_c_final_mean'] = csfm.mean()
        simulation_results_dict['sim_c_final_stdev'] = csfm.std()

        return simulation_results_dict


    def gather_group(self, effect_mean, effect_stdev):
        sample_start = np.random.normal(self.pop_mean, self.pop_stdev, self.sample_size)
        sample_effect = np.random.normal(effect_mean, effect_stdev, self.sample_size)
        sample_final = sample_start + sample_effect
        return sample_start, sample_effect, sample_final


    def gather_sample(self):
        e_sample_start, e_sample_effect, e_sample_final = self.gather_group(self.e_pop_effect_mean, self.e_pop_effect_stdev)
        c_sample_start, c_sample_effect, c_sample_final = self.gather_group(self.c_pop_effect_mean, self.c_pop_effect_stdev)
        return e_sample_start, e_sample_effect, e_sample_final, c_sample_start, c_sample_effect, c_sample_final


    def summarize_scores(self, e_sample_start, e_sample_effect, e_sample_final, c_sample_start, c_sample_effect, c_sample_final):

        all_scores = np.concatenate((e_sample_start, e_sample_final, c_sample_start, c_sample_final))
        all_improvements = np.concatenate((e_sample_effect, c_sample_effect))

        result_dict = {'sample_size': self.sample_size,
                       'e_sample_start_mean': e_sample_start.mean(),
                       'e_sample_start_stdev': e_sample_start.std(),
                       'e_sample_effect_mean': e_sample_effect.mean(),
                       'e_sample_effect_stdev': e_sample_effect.std(),
                       'e_sample_final_mean': e_sample_final.mean(),
                       'e_sample_final_stdev': e_sample_final.std(),
                       'c_sample_start_mean': c_sample_start.mean(),
                       'c_sample_start_stdev': c_sample_start.std(),
                       'c_sample_effect_mean': c_sample_effect.mean(),
                       'c_sample_effect_stdev': c_sample_effect.std(),
                       'c_sample_final_mean': c_sample_final.mean(),
                       'c_sample_final_stdev': c_sample_final.std(),
                       'max_score': all_scores.max(),
                       'min_score': all_scores.min(),
                       'max_improvement': all_improvements.max(),
                       'min_improvement': all_improvements.min()}

        result_dict['e_sample_effect_se'] = result_dict['e_sample_effect_stdev']/(self.sample_size**0.5)
        result_dict['c_sample_effect_se'] = result_dict['c_sample_effect_stdev']/(self.sample_size**0.5)
        result_dict['t'] = (result_dict['e_sample_effect_mean'] - result_dict['c_sample_effect_mean'])/((result_dict['e_sample_effect_se']**2 + result_dict['c_sample_effect_se']**2)**0.5)
        result_dict['p'] = 1-scs.t.cdf(result_dict['t'], 2*self.sample_size-1)

        return result_dict


    def reset_history(self):
        self.history_dict_list = []


def main():

    the_experiment = Experiment()

    the_display = Display(the_experiment)
    the_display.root.mainloop()


main()
