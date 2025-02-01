from block_helpers.block_to_block_type import BlockType, block_to_block_type
from inline_helpers.text_to_textnodes import text_to_textnodes
from nodes.leafnode import LeafNode
from nodes.parentnode import ParentNode
from nodes.textnode import TextNode, TextType

def map_text_nodes(text_nodes: list):
    return list(map(lambda n: n.to_html(), text_nodes))

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    lines = block.split('\n')

    match (block_type):
        case BlockType.HEADING:
            heading_num = block.count('#')
            heading_text = block.split(f"{'#'*heading_num} ")[1]
            children = map_text_nodes(text_to_textnodes(heading_text))
            return ParentNode(f'h{heading_num}', children)
        case BlockType.CODE:
            children = []
            for line in lines:
                if not line.startswith('```'):
                    children.append(LeafNode(f"{line}\n"))
            children[-1].value = children[-1].value.rstrip('\n')
            return ParentNode('pre', [ParentNode('code', children)])
        case BlockType.QUOTE:
            children = []
            for line in lines:
                if line.startswith('> '):
                    children.append(LeafNode(f"{line[2:]} "))
            children[-1].value = children[-1].value.rstrip(' ')
            return ParentNode('blockquote', children)
        case BlockType.U_LIST:
            children = []
            for line in lines:
                if line.startswith('* ') or line.startswith('- '):
                    children.append(
                        ParentNode(
                            'li',
                            map_text_nodes(
                                text_to_textnodes(line[2:])
                            ))
                    )
            return ParentNode('ul', children)
        case BlockType.O_LIST:
            children = []
            i = 1
            for line in lines:
                start = f'{i}. '
                if line.startswith(start):
                    children.append(
                        ParentNode(
                            'li',
                            map_text_nodes(
                                text_to_textnodes(line[len(start):])
                            ))
                    )
                i += 1
            return ParentNode('ol', children)
        case _:
            return ParentNode('p', map_text_nodes(text_to_textnodes(block)))