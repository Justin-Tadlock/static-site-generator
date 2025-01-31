import unittest


from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType



class SplitNodesLink(unittest.TestCase):
    def test_split_nodes_link(self):
        result = split_nodes_link([
            TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.TEXT,
            )
        ])
        self.assertListEqual(result, [
            TextNode("This is text with a link ", TextType.TEXT, None),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT, None),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ])
