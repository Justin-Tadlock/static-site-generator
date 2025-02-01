import re

def extract_markdown_images(text) -> list[tuple]:
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(regex, text)