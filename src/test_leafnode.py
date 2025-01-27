import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_raw_text(self):
        node = LeafNode("This is a leaf node")
        self.assertEqual(node.to_html(), "This is a leaf node")

    def test_to_html_p(self):
        node = LeafNode(tag="p", value="This is a paragraph node")
        self.assertEqual(node.to_html(), "<p>This is a paragraph node</p>")

    def test_to_html_anchor(self):
        node = LeafNode(tag="a", value="Click me!", props={ "href": "https://boot.dev" })
        self.assertEqual(node.to_html(), "<a href=\"https://boot.dev\">Click me!</a>")