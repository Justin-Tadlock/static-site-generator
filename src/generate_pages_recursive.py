import os

from generate_page import generate_page


def generate_pages_recursive(content_path, template_path, dest_path):
    for f in os.listdir(content_path):
        curr_path = os.path.join(content_path, f)
        if os.path.isdir(curr_path):
            new_dest = os.path.join(dest_path, f)
            if not os.path.exists(new_dest):
                os.mkdir(new_dest)
            generate_pages_recursive(curr_path, template_path, new_dest)
        else:
            generate_page(curr_path, template_path, os.path.join(dest_path, f))
