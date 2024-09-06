import tkinter as tk
from tkinter import scrolledtext
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
from io import StringIO
import os
from pathlib import Path
from bs4 import BeautifulSoup  # For parsing the generated HTML

def load_content(content_directory_path, section_list):
    content_dict = {}

    content_file_list = os.listdir(content_directory_path)
    for file_name in content_file_list:
        if not file_name.startswith('.'):
            if file_name.endswith('.txt') or file_name.endswith('.md'):
                file_path = os.path.join(content_directory_path, file_name)
                base_name = Path(file_name).stem
                file_extension = Path(file_name).suffix[1:]
                with open(file_path, 'r') as file:
                    file_contents = file.read()

                if file_name in section_list:
                    is_section = True
                else:
                    is_section = False
                content_dict[base_name] = {'file_extension': file_extension,
                                           'is_section': is_section,
                                           'content': file_contents}
    return content_dict

class MarkdownToTkinter:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.text_widget.configure(state='normal')

    def convert_markdown_to_tkinter(self, markdown_text):
        html = markdown.markdown(markdown_text)
        print()
        print(markdown_text)
        print(html)
        self.render_html_to_tkinter(html)

    def render_html_to_tkinter(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        self.text_widget.delete('1.0', tk.END)

        print("Soup Descendants")
        print(soup.prettify())
        # print()
        for element in soup.descendants:
            # print(f"Name: {element.name}, Text: {element.get_text()}")

            if element.name:  # Only process elements with tags
                if element.name == 'h1':
                    self.insert_with_tag(element.get_text(), 'heading1')
                elif element.name == 'h2':
                    self.insert_with_tag(element.get_text(), 'heading2')
                elif element.name == 'strong':
                    self.insert_with_tag(element.get_text(), 'bold')
                elif element.name == 'em':
                    self.insert_with_tag(element.get_text(), 'italic')
                elif element.name == 'p':
                    self.insert_with_tag(element.get_text() + '\n\n')
                elif element.name == 'li':
                    self.insert_with_tag("• " + element.get_text() + '\n')

        self.text_widget.configure(state='disabled')

    def insert_with_tag(self, text, tag=None):
        if tag:
            self.text_widget.insert(tk.END, text, tag)
        else:
            self.text_widget.insert(tk.END, text)