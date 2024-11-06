import numpy as np
import matplotlib.pyplot as plt
import sys

def create_scatterplot(data, params, jitter_amount=0.15):
    fig = plt.figure(figsize=(9, 6), dpi=100)
    plt.title(f'Scatterplot of Quiz Scores vs Hours Studying (n={params['num_participants']})')
    plt.xlabel('Hours Studying')
    plt.ylabel('Quiz Score')
    ax = plt.gca()
    condition_means = data.mean(0)

    num_conditions = len(params['condition_values'])
    for i in range(num_conditions):
        jitter = np.random.uniform(-jitter_amount, jitter_amount, params['num_participants'])
        x_values = params['condition_values'][i] * np.ones([params['num_participants']]) + jitter  # Jitter the x-values
        y_values = data[:, i]
        plt.scatter(x_values, y_values, alpha=0.7) # Scatter plot for each condition
        annotation = f"{condition_means[i]:.3f}" # Annotation

        # Specify the y-coordinate where the annotation should be placed
        plt.text(params['condition_values'][i], condition_means[i], annotation, fontsize=12, color='black', ha='center')

    # Set axis limits
    plt.ylim(-0.1, 1.1)  # Y-axis range from 0 to 1
    plt.xlim(-2, np.max(params['condition_values'])+2)  # X-axis range from 0 to max(condition_values)
    plt.xticks(params['condition_values'])
    plt.yticks(np.linspace(0, 1, 10))
    plt.margins(x=0.05, y=0.05)
    plt.tight_layout()
    plt.show()

def sigmoid(z, l=0.75, m=0.25, x0=0, k=10):
    p = l / (1 + np.exp(-k * (z - x0))) + m
    return p

def get_scores(params):
    num_participants = params['num_participants']
    num_questions = params['num_questions']
    condition_values = params['condition_values']
    num_conditions = len(condition_values)

    # Initialize the score matrix with shape (num_participants, num_questions, num_conditions)
    score_matrix = np.zeros((num_participants, num_questions, num_conditions), float)

    # Precompute probabilities for each condition based on condition values
    z_values = params['b0'] + params['b1'] * np.array(condition_values)
    probabilities = sigmoid(z_values, l=params['l'], m=params['m'], k=params['k'], x0=params['x0'])

    # Vectorized binomial sampling for all conditions, questions, and participants
    for k in range(num_conditions):
        p = probabilities[k]
        score_matrix[:, :, k] = np.random.binomial(1, p, (num_participants, num_questions))

    return score_matrix

def plot_sigmoid(params):
    # Find the x0 (inflection point at y=0.4)
    x_vals = np.linspace(-5, 20, 500)
    z_vals = params['b0'] + params['b1'] * x_vals
    y_vals = sigmoid(z_vals, l=params['l'], m=params['m'], k=params['k'], x0=params['x0'])

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label='Sigmoid Function')
    plt.axhline(y=0.4, color='red', linestyle='--', label='y=0.4 (inflection point)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.ylim(0, 1)  # Y-axis range from 0 to 1
    plt.xlim(-5, 20)  # X-axis range from 0 to max(condition_values)
    plt.title('Sigmoid Function with min=0.25, max=1, and inflection at y=0.4')
    plt.legend()
    plt.grid(True)
    plt.show()

def usage_example():
    print("Usage: python script.py <positive_integer>")
    print("Example: python exp.py 10")

def validate_positive_integer(input_value):
    try:
        n = int(input_value)
        if n <= 0:
            raise ValueError
    except (ValueError, IndexError):
        print("Error: Input must be a positive integer.")
        usage_example()
        sys.exit(1)  # Exit with error code 1
    return n

def main():
    if len(sys.argv) != 2:
        print("Error: Exactly one argument is required.")
        usage_example()
        sys.exit(1)

    n = validate_positive_integer(sys.argv[1])

    params = {'b0': -15,
              'b1': 5,
              'l': 0.75,
              'm': 0.25,
              'x0': .1,
              'k': .2,
              'num_participants': n,
              'num_questions': 20,
              'condition_values': np.array([0, 1, 2, 4, 8], float)}

    # plot_sigmoid(params)

    score_matrix = get_scores(params)
    participant_mean_matrix = score_matrix.mean(axis=1)

    create_scatterplot(participant_mean_matrix, params)

if __name__ == '__main__':
    main()