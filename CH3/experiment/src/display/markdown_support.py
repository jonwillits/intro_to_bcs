import tkinter as tk
from tkinter import scrolledtext
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
from io import StringIO
from bs4 import BeautifulSoup  # For parsing the generated HTML


class MarkdownToTkinter:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.text_widget.configure(state='normal')

    def convert_markdown_to_tkinter(self, markdown_text):
        html = markdown.markdown(markdown_text)
        self.render_html_to_tkinter(html)

    def render_html_to_tkinter(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        self.text_widget.delete('1.0', tk.END)
        for element in soup.descendants:
            if element.name:
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
                elif element.name == 'ul' or element.name == 'ol':
                    pass  # Handle lists if needed
                elif element.name == 'li':
                    self.insert_with_tag("• " + element.get_text() + '\n')
            else:
                self.text_widget.insert(tk.END, element)

        self.text_widget.configure(state='disabled')

    def insert_with_tag(self, text, tag=None):
        if tag:
            self.text_widget.insert(tk.END, text, tag)
        else:
            self.text_widget.insert(tk.END, text)

def setup_text_widget():
    root = tk.Tk()
    root.title("Markdown Viewer")

    text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=80)
    text_widget.pack(expand=True, fill='both')

    # Configure tags
    text_widget.tag_configure('heading1', font=('Helvetica', 16, 'bold'))
    text_widget.tag_configure('heading2', font=('Helvetica', 14, 'bold'))
    text_widget.tag_configure('bold', font=('Helvetica', 12, 'bold'))
    text_widget.tag_configure('italic', font=('Helvetica', 12, 'italic'))

    return root, text_widget

def load_markdown_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

if __name__ == "__main__":
    root, text_widget = setup_text_widget()

    # Load your markdown file here
    markdown_text = load_markdown_file("example.md")

    # Convert and display the markdown content in the Tkinter Text widget
    converter = MarkdownToTkinter(text_widget)
    converter.convert_markdown_to_tkinter(markdown_text)

    root.mainloop()
