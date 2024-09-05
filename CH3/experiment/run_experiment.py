from src.display import display
from src.display import markdown_support
from src import experiment



if __name__ == "__main__":
    content_directory_path = "content"
    section_list = ["overview.md", "linear_model.md"]
    content_dict = markdown_support.load_content(content_directory_path, section_list)
    the_experiment = experiment.Experiment()
    app = display.Display(the_experiment, section_list, content_dict)
    app.root.mainloop()