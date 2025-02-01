from nodes import TextNode, TextType
from inline_helpers import extract_markdown_links

def get_split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        node_text = node.text
        links = extract_markdown_links(node_text)
        
        for link in links:
            text, url = link
            left, right = node_text.split(f"[{text}]({url})", 1)

            if right is None:
                raise ValueError("Invalid markdown, link section not closed")
            if left != '':
                new_nodes.append(TextNode(left, TextType.TEXT))
            
            new_nodes.append(TextNode(text, TextType.LINK, url))
            node_text = right
        if len(node_text) > 0:
            new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes
