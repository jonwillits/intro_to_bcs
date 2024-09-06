import markdown
import os
from pathlib import Path
from tkinterweb import HtmlFrame


def load_content(content_directory_path, section_list):
    content_dict = {}

    content_file_list = os.listdir(content_directory_path)
    for file_name in content_file_list:
        if not file_name.startswith('.'):
            if file_name.endswith('.txt') or file_name.endswith('.md') or file_name.endswith('.html'):
                file_path = os.path.join(content_directory_path, file_name)
                base_name = Path(file_name).stem
                file_extension = Path(file_name).suffix[1:]
                with open(file_path, 'r') as file:
                    file_contents = file.read()
                    file_contents = convert_markdown_to_html(file_contents)

                if file_name in section_list:
                    is_section = True
                else:
                    is_section = False
                content_dict[base_name] = {'file_extension': file_extension,
                                           'is_section': is_section,
                                           'content': file_contents}
    return content_dict

def convert_markdown_to_html(markdown_text):
    html = markdown.markdown(markdown_text)
    return html

def create_html_frame(parent, content, height):
    html_frame = HtmlFrame(parent, height=height)
    html_frame.pack(fill="x", expand=True)
    html_frame.load_html(content)
