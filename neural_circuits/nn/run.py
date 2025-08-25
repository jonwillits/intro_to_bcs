import numpy as np
import params
from src import network, dataset
from src.app import app


def main():

    the_dataset = dataset.Dataset(dataset_type=params.Dataset.dataset_type)
    the_network = network.NeuralNetwork(params.Network)
    np.set_printoptions(suppress=True, precision=3)
    the_display = app.App(params.App, the_network, the_dataset)
    the_display.root.mainloop()



main()
