from src import datasets
from src.app import app
from src import network
import params
import numpy as np

# Set print options
np.set_printoptions(
    threshold=np.inf,       # Show all elements
    linewidth=np.inf,       # No wrapping
    # precision=3,            # Set precision to 3 decimal places
    suppress=True           # Avoid scientific notation
)

def main():
    training_set = datasets.Shapes(params.Shapes)
    test_set = datasets.Shapes(params.Shapes)
    the_network = network.Network(params)
    the_app = app.App(the_network, training_set, test_set, params)
    the_app.root.mainloop()


if __name__ == '__main__':
    main()