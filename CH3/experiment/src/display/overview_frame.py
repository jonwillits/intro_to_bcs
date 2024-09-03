from . import content_frame


class OverviewFrame(content_frame.ContentFrame):

    def __init__(self, display, frame_name):
        super().__init__(display, frame_name)
        text = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras a arcu vel mauris interdum eleifend. 
        Vestibulum placerat scelerisque arcu, non ornare eros sagittis vel. Cras mollis augue nec massa sagittis 
        suscipit. Nulla a nisl a orci maximus sollicitudin. Vivamus non libero ante. Cras finibus fringilla nisi, id 
        interdum velit bibendum in. Etiam nec elementum lacus. Aliquam fermentum hendrerit porta. In id libero aliquam, 
        placerat dui quis, consectetur nisl. Aenean vitae arcu sit amet justo eleifend hendrerit. Pellentesque lorem 
        risus, varius eget aliquet vel, convallis ac augue. 
        """

        self.overview_label = content_frame.ResizableLabelFrame(self.frame, text)
        self.overview_label.place(x=10, y=100, relwidth=1, relheight=1)
