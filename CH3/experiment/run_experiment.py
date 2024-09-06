from src.display import app
from src.display import markdown_support
from src import experiment



if __name__ == "__main__":
    width = 950
    height = 600
    content_directory_path = "content"
    section_list = ["overview.md", "linear_model.md"]
    content_dict = markdown_support.load_content(content_directory_path, section_list)
    the_experiment = experiment.Experiment()
    app = app.App(the_experiment, section_list, content_dict, width, height)
    app.root.mainloop()