from src.display import display
from src.display import markdown_support
from src import experiment
from pathlib import Path
import os



if __name__ == "__main__":
    content_dict = markdown_support.load_content()
    the_experiment = experiment.Experiment()
    app = display.Display(the_experiment, content_dict)
    app.root.mainloop()