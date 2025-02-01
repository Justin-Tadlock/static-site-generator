from inline_helpers import get_delimited_slices
from nodes import TextNode, TextType

def get_split_nodes(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        node_text = node.text
        while len(node_text) > 0:
            first, delim, remainder = get_delimited_slices(node_text, delimiter)
            if first == '' and delim == '':
                new_nodes.append(TextNode(remainder, TextType.TEXT))
                break
            
            if first != '':
                first_node = TextNode(first, TextType.TEXT)
                new_nodes.append(first_node)

            match text_type:
                case TextType.LINK:
                    delimited_node = TextNode(delim, text_type, url=node.url)
                case TextType.IMAGE:
                    delimited_node = TextNode(None, text_type, { 'href': node.url, 'alt': delim})
                case _:
                    delimited_node = TextNode(delim, text_type)
            new_nodes.append(delimited_node)            

            node_text = remainder
    return new_nodes


