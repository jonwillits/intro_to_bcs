# def adjust_frame_size(frame, frame_padding):
#     # Get the bounding box (min/max coordinates of all children)
#     max_x, max_y = 0, 0
#     for widget in frame.winfo_children():
#         # Get widget's coordinates and size
#         widget.update_idletasks()  # Ensure that geometry info is updated
#         x = widget.winfo_x()
#         y = widget.winfo_y()
#         width = widget.winfo_width()
#         height = widget.winfo_height()
#
#         # Determine the bottom-right corner of the widget
#         max_x = max(max_x, x + width)
#         max_y = max(max_y, y + height)
#
#     # Set the frame size to fit all children
#     frame.config(width=max_x + frame_padding, height=max_y + frame_padding)