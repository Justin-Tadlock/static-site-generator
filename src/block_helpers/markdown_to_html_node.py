from block_helpers.markdown_to_blocks import markdown_to_blocks
from block_helpers.block_to_block_type import block_to_block_type
from block_helpers.block_to_html_node import block_to_html_node
from nodes.htmlnode import HTMLNode
from nodes.parentnode import ParentNode


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    children = []
    for block in blocks:
        children.append(block_to_html_node(block))
    
    return ParentNode('div', children)
