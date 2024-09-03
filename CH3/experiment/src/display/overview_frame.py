from . import content_frame
import tkinter as tk

class OverviewFrame(content_frame.ContentFrame):

    def __init__(self, display, frame_name):
        super().__init__(display, frame_name)
        self.frame_padding = 20
        text = self.display.content_dict['overview']
        label = content_frame.ResizableLabel(self.frame,
                                             text=text,
                                             x=self.frame_padding,
                                             y=50,
                                             bg="white",
                                             fg="black",
                                             anchor="nw",
                                             justify="left",
                                             padding=self.frame_padding)
