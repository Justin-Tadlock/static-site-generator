import re

from textnode import TextNode, TextType
from helpers import extract_markdown_images

def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []

    for node in old_nodes:
        images = extract_markdown_images(node.text)
        results = []

        remainder = node.text
        for image in images:
            text, url = image
            left, right = remainder.split(f"![{text}]({url})")

            results.append(TextNode(left, TextType.TEXT))
            results.append(TextNode(text, TextType.IMAGE, url))
            remainder = right
        if len(remainder) > 0:
            results.append(TextNode(remainder, TextType.TEXT))
        new_nodes.extend(results)
    return new_nodes
