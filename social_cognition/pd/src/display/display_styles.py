# src/styles.py
"""
Centralized Tkinter styles for the PD GUI.

Exposes:
- COLORS.MENU_BG / COLORS.CONTENT_BG
- MENU_BUTTON: style for buttons in the top menu
- CONTENT_BUTTON: style for buttons in the content area
- CONTENT_TEXT: style for text labels in the content area
- OPTIONMENU: style for the OptionMenu + its dropdown
- apply_optionmenu_style(widget, style): helper to apply OPTIONMENU to both the
  visible control and its internal Menu widget
"""

import tkinter as tk

class COLORS:
    MENU_BG    = "#20232a"
    CONTENT_BG = "#f5f6f7"

# Base font choices (tweak if you want)
BASE_FONT = ("Consolas", 16, "normal")
SMALL_FONT = ("Consolas", 11, "normal")
TITLE_FONT = ("Consolas", 18, "bold")

# Flat / minimal, dark buttons for the top menu
MENU_BUTTON = dict(
    relief="flat",
    bd=0,
    highlightthickness=0,
    overrelief="flat",
    width=10,
    bg="#333333",
    fg="#000000",
    activebackground="#444444",
    activeforeground="#ffffff",
    disabledforeground="#777777",
    font=("Consolas", 16, "bold"),
    padx=12,
    pady=6,
)

# Flat / minimal, dark buttons for the content area
CONTENT_BUTTON = dict(
    relief="flat",
    bd=0,
    highlightthickness=0,
    overrelief="flat",
    bg="#3a3a3a",
    fg="#000000",
    width=5,
    activebackground="#4a4a4a",
    activeforeground="#ffffff",
    disabledforeground="#888888",
    font=BASE_FONT,
    padx=12,
    pady=8,
)

# Standard content text labels
CONTENT_TEXT = dict(
    bg=COLORS.CONTENT_BG,
    activebackground=COLORS.CONTENT_BG,
    fg="#000000",
    font=("Consolas", 20)
)

# Standard content text labels
TOURNAMENT_SCORE_TEXT = dict(
    bg=COLORS.CONTENT_BG,
    activebackground=COLORS.CONTENT_BG,
    fg="#000000",
    font=("Consolas", 16)
)

CONTENT_TEXT_ENTRY = dict(
    bg=COLORS.CONTENT_BG,
    fg="#000000",
    font=("Consolas", 20),
    # activebackground=COLORS.CONTENT_BG,
)

# OptionMenu styling (control + dropdown menu)
OPTIONMENU = dict(
    control=dict(
        relief="flat",
        bd=0,
        padx=0,
        pady=0,
        highlightthickness=0,
        bg="#000000",
        fg="#ffffff",
        activebackground="#f5f6f7",
        activeforeground="#f5f6f7",
        font=TITLE_FONT,
        borderwidth=0,  # remove sunken border
    ),
    menu=dict(
        tearoff=False,
        bg="#2b2b2b",
        fg="#ffffff",
        font=TITLE_FONT,
        activebackground="#3a3a3a",
        activeforeground="#ffffff",
        borderwidth=0,
    ),
)

def apply_optionmenu_style(optionmenu: tk.OptionMenu, style: dict) -> None:
    """Apply OPTIONMENU styles to the OptionMenu and its internal Menu."""
    ctrl = style.get("control", {})
    menu_cfg = style.get("menu", {})

    # Style the visible OptionMenu button
    optionmenu.configure(**ctrl)

    # Style the dropdown menu (tk.Menu)
    m = optionmenu["menu"]
    if isinstance(m, tk.Menu):
        m.configure(
            tearoff=menu_cfg.get("tearoff", False),
            bg=menu_cfg.get("bg", "#2b2b2b"),
            fg=menu_cfg.get("fg", "#ffffff"),
            activebackground=menu_cfg.get("activebackground", "#3a3a3a"),
            activeforeground=menu_cfg.get("activeforeground", "#ffffff"),
            borderwidth=menu_cfg.get("borderwidth", 0),
            relief=menu_cfg.get("relief", "flat"),
        )