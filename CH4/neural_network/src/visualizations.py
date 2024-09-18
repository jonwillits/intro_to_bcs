import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_dataset(training_set, test_set):
    # Color map: blue (#0000ff) for y=1, orange (#ff7f0e) for training set
    # and green (#00ff00) for y=1, red (#ff0000) for y=0 for test set
    training_set_colors = {1: '#0000ff', 0: '#ff7f0e'}
    test_set_colors = {1: '#0000ff', 0: '#ff7f0e'}

    # Create a scatter plot using dataset.x and dataset.y for training and test sets
    plt.scatter(training_set.x[:, 0], training_set.x[:, 1],
                c=[training_set_colors[val] for val in training_set.y], label="Training Set")
    plt.scatter(test_set.x[:, 0], test_set.x[:, 1],
                c=[test_set_colors[val] for val in test_set.y], label="Test Set", marker='x')

    # Add labels and title
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Scatter plot of x1 vs x2')

    # Create legend elements using the colors from the color dictionaries
    training_y1_patch = mpatches.Patch(color=training_set_colors[1], label='Training 1')
    training_y0_patch = mpatches.Patch(color=training_set_colors[0], label='Training 0')
    test_y1_patch = mpatches.Patch(color=test_set_colors[1], label='Test 1')
    test_y0_patch = mpatches.Patch(color=test_set_colors[0], label='Test 0')

    # Add the legend
    plt.legend(handles=[training_y1_patch, training_y0_patch, test_y1_patch, test_y0_patch])

    # Show the plot
    plt.show()
