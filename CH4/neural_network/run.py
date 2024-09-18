from src import dataset
from src import visualizations
from src import app
from src import network
import params

def main():
    app_dimensions = (900, 650)

    training_set, test_set = dataset.generate_dataset(params.Dataset)
    #visualizations.plot_dataset(training_set, test_set)
    # the_network = network.BasicNetwork(training_set)
    # the_network.train(params.NeuralNetwork, training_set, test_set)

    the_network = network.BetterNetwork(params.NeuralNetwork, training_set)
    the_network.train(training_set, test_set)
    # print(the_network)
    # the_app = app.App()
    # the_app.root.mainloop()

if __name__ == "__main__":
    main()
