import os
import shutil

from block_helpers.extract_title import extract_title
from block_helpers.markdown_to_html_node import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path, 'r') as from_file:
        from_content = from_file.read()

    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    md_title = extract_title(from_content)
    md_to_html = markdown_to_html_node(from_content).to_html()

    template_result = template_content.replace(
        '{{ Title }}', md_title
        ).replace(
            '{{ Content }}', md_to_html
            )
    
    if not os.path.exists(os.path.abspath(os.path.dirname(dest_path))):
        os.mkdir(os.path.abspath(os.path.dirname(dest_path)))
    with open(dest_path.replace('.md', '.html'), 'w') as out_file:
        out_file.write(template_result)
    
    
    