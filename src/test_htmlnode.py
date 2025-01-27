import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr_tag_only(self):
        node = HTMLNode(tag="h1")
        self.assertEqual(node.__repr__(), "HTMLNode(h1, None, None, None)")

    def test_repr_value_only(self):
        node = HTMLNode(value="Heading Text")
        self.assertEqual(node.__repr__(), "HTMLNode(None, Heading Text, None, None)")

    def test_repr_children_only(self):
        node = HTMLNode(children=[HTMLNode(value="Child Text")])
        self.assertEqual(node.__repr__(), "HTMLNode(None, None, [HTMLNode(None, Child Text, None, None)], None)")

    def test_repr_props_only(self):
        node = HTMLNode(props={"class": "heading"})
        self.assertEqual(node.__repr__(), "HTMLNode(None, None, None, {'class': 'heading'})")

    def test_props_to_html(self):
        node = HTMLNode(props={"class": "heading", "color": "red"})
        self.assertEqual(node.props_to_html(), " class=\"heading\" color=\"red\"")

    def test_to_html(self):
        node = HTMLNode(tag="h1", value="Hello world")
        self.assertRaises(NotImplementedError, node.to_html)