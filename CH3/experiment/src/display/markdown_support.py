import markdown


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