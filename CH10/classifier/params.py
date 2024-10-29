class Shapes:

    instances_per_category = 500
    noise = .4
    image_size = 64
    category_list = ['triangle', 'rectangle', 'square', 'rhombus', 'trapezoid',
                     'pentagon', 'hexagon', 'circle', 'oval', 'star']

class Network:
    hidden_size = 64
    num_epochs = 2000
    learning_rate = 0.0001
    output_freq = 1
    l2_lambda = .05
    batch_size = 256

class App:
    network_frame_padding = 20
    network_frame_border = 2
    network_frame_highlight_thickness = 2

    layer_spacing = 50
    layer_max_rows = 8

    input_layer_border = 0
    input_layer_highlight_thickness = 3

    hidden_frame_padding = 5
    hidden_frame_border = 0
    hidden_frame_highlight_thickness = 3

    output_frame_padding = 5
    output_frame_border = 0
    output_frame_highlight_thickness = 3
    output_label_width = 60

    hidden_bias_offset = 5
    hidden_bias_border = 0
    hidden_bias_highlight_thickness = 3

    output_bias_offset = 5
    output_bias_border = 0
    output_bias_highlight_thickness = 3

    unit_size = 20
    unit_spacing = 0
    unit_border = 0
    unit_highlight_thickness = 2
    unit_label_offset = 20
