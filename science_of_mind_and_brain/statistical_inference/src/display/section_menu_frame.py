import tkinter as tk

class SectionMenuFrame:
    def __init__(self, app):
        self.app = app

        self.button_padding = 2
        self.button_font = ("Helvetica", 10)
        self.button_fg = "black"
        self.button_bg = "#FF5F05"
        self.button_highlight_fg = "white"
        self.button_highlight_bg = "#13294B"

        # Create the section frame with a background color and fixed width
        self.section_menu_frame = tk.Frame(self.app.root,
                                           bg="#707372",
                                           borderwidth=2,
                                           highlightbackground="black",
                                           highlightthickness=2,
                                           relief="solid",
                                           width=self.app.section_frame_dimensions[0])

        # Pack the section_frame
        self.section_menu_frame.pack(side="left", fill="y", expand=False)  # Vertical expansion only

        # Add the section buttons
        for i, section in enumerate(self.app.the_params.section_list):
            title = section['title']
            label = tk.Label(self.section_menu_frame,
                             anchor="w",
                             text=title,
                             fg=self.button_fg,
                             bg=self.button_bg,
                             font=self.button_font,
                             padx=self.button_padding,
                             pady=self.button_padding,
                             borderwidth=2,
                             relief="flat")

            label.bind("<Button-1>", lambda event, index=i, lbl=label: self.on_section_click(lbl, index))
            label.pack(side="top", fill="x", pady=1)

        # Quit label to act like a button
        self.quit_label = tk.Label(self.section_menu_frame,
                                   text="Quit",
                                   fg=self.button_fg,
                                   bg=self.button_bg,
                                   font=self.button_font,
                                   padx=self.button_padding,
                                   pady=self.button_padding,
                                   borderwidth=2,
                                   relief="flat")

        # Bind left mouse click to the Quit label
        self.quit_label.bind("<Button-1>", lambda event, lbl=self.quit_label: self.on_quit_click(lbl))

        # Pack the Quit label at the bottom
        self.quit_label.pack(side="bottom", fill="x", pady=10)

    def highlight_button(self, label):
        original_bg = label.cget("bg")  # Get the original bg color
        original_fg = label.cget("fg")  # Get the original fg color

        # Change the label background to a new color
        label.config(bg=self.button_highlight_bg)  # Set the temporary bg color
        label.config(fg=self.button_highlight_fg)  # Set the temporary fg color

        # Change the background back to the original color after 300ms
        self.section_menu_frame.after(300, lambda: label.config(bg=original_bg, fg=original_fg))

    def on_quit_click(self, label):
        self.highlight_button(label)
        # Delay quitting the app by 300ms to allow the highlight effect to be visible
        self.section_menu_frame.after(350, self.app.quit)

    def on_section_click(self, label, index):
        """Handle label click and change its background color temporarily."""
        self.highlight_button(label)
        self.app.show_section(index) # Show the corresponding content frame
