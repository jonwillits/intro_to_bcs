from src import datasets
from src.app import app
from src import network
import params

def main():
    the_dataset = datasets.Shapes(params.Shapes)
    the_network = network.Network(params.Network, the_dataset.image_size**2, the_dataset.num_categories)
    the_app = app.App(the_network, the_dataset)
    the_app.root.mainloop()


if __name__ == '__main__':
    main()