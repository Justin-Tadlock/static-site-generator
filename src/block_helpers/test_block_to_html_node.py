import unittest

from nodes.leafnode import LeafNode
from nodes.parentnode import ParentNode

from .block_to_html_node import block_to_html_node

class TestBlockToHtmlNode(unittest.TestCase):
    def test_block_to_heading(self):
        for i in range(1,7):
            self.assertEqual(
                block_to_html_node(f"{'#' * i} Heading").to_html(),
                LeafNode('Heading', f'h{i}').to_html()
            )
    
    def test_block_to_code(self):
        child_node = "const nothing = () => 'to see here'"
        self.assertEqual(
            block_to_html_node(
                f"```\n{child_node}\n```"
            ).to_html(),
            ParentNode('pre', [
                ParentNode('code', [
                    LeafNode(child_node)
                ])
            ]).to_html()
        )

    def test_block_to_quote(self):
        self.assertEqual(
            block_to_html_node('> testing\n> some quote').to_html(),
            ParentNode(
                'blockquote',
                [LeafNode('testing '), LeafNode('some quote')]
            ).to_html()
        )

    def test_block_to_ul(self):
        self.assertEqual(
            block_to_html_node('* testing\n* two lines').to_html(),
            ParentNode('ul', [
                LeafNode('testing', 'li'),
                LeafNode('two lines', 'li'),
            ]).to_html()
        )

    def test_block_to_ol(self):
        self.assertEqual(
            block_to_html_node('1. testing\n2. two lines').to_html(),
            ParentNode('ol', [
                LeafNode('testing', 'li'),
                LeafNode('two lines', 'li'),
            ]).to_html()
        )

    def test_block_to_paragraph(self):
        self.assertEqual(
            block_to_html_node('test').to_html(),
            LeafNode('test', 'p').to_html()
        )