from src.display import display
from src import experiment

if __name__ == "__main__":
    the_experiment = experiment.Experiment()
    app = display.Display(the_experiment)
    app.root.mainloop()