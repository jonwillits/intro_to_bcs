class App:
    dimensions = (900,600)
    random_seed = None

class NeuralNetwork:
    hidden_size_list = [8]
    learning_rate = 0.2
    shuffle_training_set = True
    batch_size = 1
    num_epochs = 10000
    cost_function = "mse"
    eval_freq = 1000
    verbose = False

class Dataset:
    x_range = 5
    n = 10
    noise = 0.0
    radius = 5
    dataset_type = "one_d"