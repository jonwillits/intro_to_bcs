
def calculate_layer_frame_dimensions(frame_padding, layer_dimensions, layer_border, layer_highlight_thickness,
                                     unit_size, unit_spacing, unit_border, unit_highlight_thickness, label_list=None, label_width=None):
    width = 2 * frame_padding + 2 * layer_border + 2 * layer_highlight_thickness
    width += layer_dimensions[1] * (unit_size + unit_highlight_thickness + 2 * unit_border)
    width += (layer_dimensions[1] - 1) * unit_spacing
    if label_width is not None:
        width += label_width

    height = 2 * frame_padding + 2 * layer_border + 2 * layer_highlight_thickness
    height += layer_dimensions[0] * (unit_size + unit_highlight_thickness + 2 * unit_border)
    height += (layer_dimensions[0] - 1) * unit_spacing
    frame_dimensions = (width, height)
    return frame_dimensions