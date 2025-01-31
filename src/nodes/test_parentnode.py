import unittest

from nodes import HTMLNode, LeafNode, ParentNode, TextNode, TextType

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_to_html_plain_text(self):
        node = ParentNode("div", [LeafNode(value="Hello world")])
        self.assertEqual(node.to_html(), "<div>Hello world</div>")
    
    def test_to_html_with_p_leaf(self):
        node = ParentNode("div", [LeafNode(tag="p", value="Hello world")])
        self.assertEqual(node.to_html(), "<div><p>Hello world</p></div>")
    
    def test_to_html_with_p_and_b_leafnodes(self):
        node = ParentNode("div", [
            LeafNode(tag="p", value="Hello world"),
            LeafNode(tag="b", value="Hello BOLD world")
        ])
        self.assertEqual(node.to_html(), "<div><p>Hello world</p><b>Hello BOLD world</b></div>")
    
    def test_to_html_with_nested_parentnode(self):
        node = ParentNode("div", [
            ParentNode(tag="p", children=[
                LeafNode(tag=None, value="Hello world"),
                LeafNode(tag="b", value="Hello BOLD world"),
                LeafNode(tag=None, value="Hello plain world")
            ])
        ])
        self.assertEqual(node.to_html(), "<div><p>Hello world<b>Hello BOLD world</b>Hello plain world</p></div>")