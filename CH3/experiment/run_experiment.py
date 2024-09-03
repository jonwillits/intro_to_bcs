from src.display import display
from src import experiment
from pathlib import Path
import os

def load_content():
    content_dict = {}

    dir_name = "content"
    content_file_list = os.listdir(dir_name)
    for file_name in content_file_list:
        if not file_name.startswith('.'):
            if file_name.endswith('.txt'):
                file_path = os.path.join(dir_name, file_name)
                base_name = Path(file_name).stem
                with open(file_path, 'r') as file:
                    file_contents = file.read()
                content_dict[base_name] = file_contents
    return content_dict


if __name__ == "__main__":
    content_dict = load_content()
    the_experiment = experiment.Experiment()
    app = display.Display(the_experiment, content_dict)
    app.root.mainloop()