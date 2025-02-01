from enum import Enum

from nodes import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (other.text == self.text and
            other.text_type == self.text_type and
            other.url == self.url
        ):
            return True
        return False

    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(value=text_node.text)
            case TextType.BOLD:
                return LeafNode(value=text_node.text, tag="b")
            case TextType.ITALIC:
                return LeafNode(value=text_node.text, tag="i")
            case TextType.CODE:
                return LeafNode(value=text_node.text, tag="code")
            case TextType.LINK:
                return LeafNode(value=text_node.text, tag="a", props={ "href": text_node.url })
            case TextType.IMAGE:
                return LeafNode(value="", tag="img", props={ "src": text_node.url, "alt": text_node.text })
            case _:
                raise Exception("invalid text type")

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'