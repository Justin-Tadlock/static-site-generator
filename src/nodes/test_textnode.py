import unittest

from nodes import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)
    
    def test_eq_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node, node2)
    
    def test_eq_link(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node, node2)
    
    def test_eq_image(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertEqual(node, node2)

    def test_neq_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)
    
    def test_neq_bold_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node, node2)
    
    def test_neq_content(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_to_htmlnode_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.__repr__(), "HTMLNode(None, This is a text node, None, None)")

    def test_to_htmlnode_bold(self):
        node = TextNode("This is a BOLD text node", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.__repr__(), "HTMLNode(b, This is a BOLD text node, None, None)")

    def test_to_htmlnode_italic(self):
        node = TextNode("This is an ITALIC text node", TextType.ITALIC)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.__repr__(), "HTMLNode(i, This is an ITALIC text node, None, None)")

    def test_to_htmlnode_code(self):
        node = TextNode("This is a CODE text node", TextType.CODE)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.__repr__(), "HTMLNode(code, This is a CODE text node, None, None)")

    def test_to_htmlnode_LINK(self):
        node = TextNode("This is a LINK text node", TextType.LINK, "http://boot.dev")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.__repr__(), "HTMLNode(a, This is a LINK text node, None, {'href': 'http://boot.dev'})")

    def test_to_htmlnode_image(self):
        node = TextNode("This is an IMAGE text node", TextType.IMAGE, 'http://boot.dev')
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.__repr__(), "HTMLNode(img, , None, {'src': 'http://boot.dev', 'alt': 'This is an IMAGE text node'})")

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.__repr__(), "TextNode(This is a text node, b, None)")


if __name__ == "__main__":
    unittest.main()