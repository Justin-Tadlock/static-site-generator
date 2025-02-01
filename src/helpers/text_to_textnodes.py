
from helpers import get_split_nodes_link, get_split_nodes_image
from helpers.split_nodes import get_split_nodes
from nodes.textnode import TextNode, TextType


def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)

    bold_nodes = get_split_nodes([text_node], "**", TextType.BOLD)
    italic_nodes = get_split_nodes(bold_nodes, "*", TextType.ITALIC)
    code_nodes = get_split_nodes(italic_nodes, "`", TextType.CODE)
    link_nodes = get_split_nodes_link(code_nodes)
    image_nodes = get_split_nodes_image(link_nodes)

    return image_nodes
