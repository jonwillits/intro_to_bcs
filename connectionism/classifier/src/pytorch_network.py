import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F


class Network(nn.Module):
    def __init__(self, input_size, hidden_sizes, output_size):
        super(Network, self).__init__()
        self.layers = nn.ModuleList()

        previous_size = input_size
        for hidden_size in hidden_sizes:
            self.layers.append(nn.Linear(previous_size, hidden_size))
            previous_size = hidden_size

        self.output_layer = nn.Linear(previous_size, output_size)

    def forward(self, x):
        x = x.view(x.size(0), -1)  # Flatten the input to (batch_size, input_size)
        for layer in self.layers:
            x = F.relu(layer(x))
        x = self.output_layer(x)
        return x

    def train_model(self, train_loader, criterion, optimizer, epochs):
        """
        Trains the model using the given data loader, loss function, and optimizer.

        Parameters:
            train_loader (DataLoader): DataLoader containing the training data.
            criterion (loss function): Loss function, e.g., CrossEntropyLoss.
            optimizer (torch.optim): Optimizer, e.g., Adam or SGD.
            epochs (int): Number of training epochs.
        """
        self.train()  # Set the model to training mode
        for epoch in range(epochs):
            running_loss = 0.0
            correct_predictions = 0
            total_predictions = 0

            for images, labels in train_loader:
                optimizer.zero_grad()  # Zero gradients
                outputs = self(images)
                loss = criterion(outputs, labels)
                loss.backward()  # Backpropagation
                optimizer.step()  # Update weights

                # Calculate metrics
                running_loss += loss.item()
                correct_predictions += (outputs.argmax(1) == labels).sum().item()
                total_predictions += labels.size(0)

            # Epoch summary
            epoch_loss = running_loss / len(train_loader)
            epoch_accuracy = 100 * correct_predictions / total_predictions
            print(f"Epoch {epoch + 1}/{epochs} - Loss: {epoch_loss:.4f} - Accuracy: {epoch_accuracy:.2f}%")

    def evaluate(self, test_loader, criterion):
        """
        Evaluates the model on the test set.

        Parameters:
            test_loader (DataLoader): DataLoader containing the test data.
            criterion (loss function): Loss function, e.g., CrossEntropyLoss.

        Returns:
            Tuple containing the average test loss and accuracy.
        """
        self.eval()  # Set the model to evaluation mode
        test_loss = 0.0
        correct_predictions = 0
        total_predictions = 0

        with torch.no_grad():  # Disable gradient computation for evaluation
            for images, labels in test_loader:
                outputs = self(images)
                loss = criterion(outputs, labels)
                test_loss += loss.item()
                correct_predictions += (outputs.argmax(1) == labels).sum().item()
                total_predictions += labels.size(0)

        average_loss = test_loss / len(test_loader)
        accuracy = 100 * correct_predictions / total_predictions
        print(f"Test Loss: {average_loss:.4f} - Test Accuracy: {accuracy:.2f}%")
        return average_loss, accuracy
