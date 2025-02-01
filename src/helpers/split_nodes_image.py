from nodes import TextNode, TextType
from helpers import extract_markdown_images

def get_split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        node_text = node.text
        images = extract_markdown_images(node_text)
        
        for image in images:
            text, url = image
            left, right = node_text.split(f"![{text}]({url})", 1)

            if right is None: 
                raise ValueError("Invalid markdown, link section not closed")
            if left != '':
                new_nodes.append(TextNode(left, TextType.TEXT))
            
            new_nodes.append(TextNode(text, TextType.IMAGE, url))
            node_text = right
        if len(node_text) > 0:
            new_nodes.append(TextNode(node_text, TextType.TEXT))
    return new_nodes
