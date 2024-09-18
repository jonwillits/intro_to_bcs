import numpy as np
import params
from src import network, dataset
from src.app import app


def main():

    the_dataset = dataset.Dataset(dataset_type=params.Dataset.dataset_type)
    the_network = network.NeuralNetwork(params.Network)
    print(the_dataset.x, the_dataset.y)
    np.set_printoptions(suppress=True, precision=3)
    # the_display = app.App(params, the_network, the_datasets)
    # the_display.root.mainloop()



main()
