import unittest

from nodes import TextNode, TextType
from .split_nodes_image import split_nodes_image

class SplitNodesImage(unittest.TestCase):
    def test_split_nodes_image(self):
        result = split_nodes_image([
            TextNode(
                "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
                TextType.TEXT,
            )
        ])
        self.assertListEqual(result, [
            TextNode("This is text with a ", TextType.TEXT, None),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT, None),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ])
