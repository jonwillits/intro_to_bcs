import markdown
from pathlib import Path
from tkinterweb import HtmlFrame


def load_content(file_path):

    file_extension = Path(file_path).suffix[1:]
    with open(file_path, 'r', encoding='utf-8') as f:

        file_contents = f.read()

    if file_extension == "md":
        file_contents = convert_markdown_to_html(file_contents)
    elif file_contents == 'txt' or file_contents == 'html':
        file_contents = file_contents
    else:
        raise Exception(f"ERROR: Unrecognized content file type {file_extension} for {file_path}")

    return file_contents

def convert_markdown_to_html(markdown_text, bg_color="pink", font_color="black",
                             h1_size="32px", h2_size="28px", h3_size="24px", p_size="16px"):
    # Convert the markdown to HTML
    html_content = markdown.markdown(markdown_text)

    # Generate the style tag by calling the separate function
    style_tag = generate_style_tag(bg_color, font_color, h1_size, h2_size, h3_size, p_size)

    # Create the full HTML template
    html_template = f"""
    <html>
    <head>
        {style_tag}
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    return html_template


def create_html_frame(parent, content, height):
    # Create the HtmlFrame
    html_frame = HtmlFrame(parent, messages_enabled=False)

    # Load the HTML content
    html_frame.load_html(content)

    # Initially set the height
    html_frame.place(x=0, y=0, relwidth=1, height=height)

    # Ensure the widget is rendered before getting the height
    html_frame.update_idletasks()

    return html_frame


def generate_style_tag(bg_color, font_color, h1_size, h2_size, h3_size, p_size):
    style_tag = f"""
    <style>
        body {{
            background-color: {bg_color};
            font-family: Arial, sans-serif;
        }}
        h1 {{
            color: {font_color};
            font-size: {h1_size};
        }}
        h2 {{
            color: {font_color};
            font-size: {h2_size};
        }}
        h3 {{
            color: {font_color};
            font-size: {h3_size};
        }}
        p {{
            color: {font_color};
            font-size: {p_size};
        }}
        li {{
            color: {font_color};
            font-size: {p_size};
        }}
    </style>
    """
    return style_tag