from src import datasets
from src.app import app
#from src import network
from src import pytorch_network
import params
import numpy as np
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim

# Set print options
np.set_printoptions(
    threshold=np.inf,       # Show all elements
    linewidth=np.inf,       # No wrapping
    # precision=3,            # Set precision to 3 decimal places
    suppress=True           # Avoid scientific notation
)

def main():
    # Set image size and other params as needed
    params.Shapes.image_size = 64  # Assuming 64x64 images
    params.Shapes.category_list = [...]  # Define categories

    # Initialize datasets and data loaders
    train_shapes = datasets.Shapes(params)
    train_dataset = datasets.ShapesDataset(train_shapes)
    test_shapes = datasets.Shapes(params)
    test_dataset = datasets.ShapesDataset(test_shapes)

    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=len(test_dataset))

    # Define network parameters
    input_size = params.Shapes.image_size ** 2  # 4096 for 64x64 image
    hidden_sizes = [128, 64]
    output_size = len(params.Shapes.category_list)

    # Initialize network, loss function, and optimizer
    network = pytorch_network.Network(input_size, hidden_sizes, output_size)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(network.parameters(), lr=0.001)

    # Train the model
    network.train_model(train_loader, criterion, optimizer, epochs=10)

    # Evaluate the model
    test_loss, test_accuracy = network.evaluate(test_loader, criterion)



if __name__ == '__main__':
    main()