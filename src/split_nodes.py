from delimited_slices import get_delimited_slices
from textnode import TextNode, TextType

def get_split_nodes(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        parsed_text = node.text

        while len(parsed_text) > 0:
            first, delim, remainder = get_delimited_slices(parsed_text, delimiter)
            if first == '' or delim == '':
                new_nodes.append(TextNode(remainder, TextType.TEXT))
                break
            
            first_node = TextNode(first, TextType.TEXT)
            match text_type:
                case TextType.LINK:
                    delimited_node = TextNode(delim, text_type, url=node.url)
                case TextType.IMAGE:
                    delimited_node = TextNode(None, text_type, { 'href': node.url, 'alt': delim})
                case _:
                    delimited_node = TextNode(delim, text_type)
            new_nodes.extend([first_node, delimited_node])

            parsed_text = remainder
        
    return new_nodes


