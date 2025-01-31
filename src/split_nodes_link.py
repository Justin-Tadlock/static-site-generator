import re

from textnode import TextNode, TextType
from helpers import extract_markdown_links

def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []

    for node in old_nodes:
        links = extract_markdown_links(node.text)
        results = []

        remainder = node.text
        for link in links:
            text, url = link
            left, right = remainder.split(f"[{text}]({url})")

            results.append(TextNode(left, TextType.TEXT))
            results.append(TextNode(text, TextType.LINK, url))
            remainder = right
        if len(remainder) > 0:
            results.append(TextNode(remainder, TextType.TEXT))
        new_nodes.extend(results)
    return new_nodes
