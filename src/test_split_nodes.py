import unittest

from split_nodes import get_split_nodes
from textnode import TextNode, TextType

class SplitNodes(unittest.TestCase):
    def test_bold(self):
        old_nodes = [
            TextNode('Testing **bold** text split', TextType.TEXT)
        ]
        split_nodes = get_split_nodes(old_nodes, '**', TextType.BOLD)
        self.assertEqual(split_nodes, [
            TextNode('Testing ', TextType.TEXT),
            TextNode('bold', TextType.BOLD),
            TextNode(' text split', TextType.TEXT)
        ])

    def test_italic(self):
        old_nodes = [
            TextNode('Testing *italic* text split', TextType.TEXT)
        ]
        split_nodes = get_split_nodes(old_nodes, '*', TextType.ITALIC)
        self.assertEqual(split_nodes, [
            TextNode('Testing ', TextType.TEXT),
            TextNode('italic', TextType.ITALIC),
            TextNode(' text split', TextType.TEXT)
        ])

    def test_code(self):
        old_nodes = [
            TextNode('Testing `code` text split', TextType.TEXT)
        ]
        split_nodes = get_split_nodes(old_nodes, '`', TextType.CODE)
        self.assertEqual(split_nodes, [
            TextNode('Testing ', TextType.TEXT),
            TextNode('code', TextType.CODE),
            TextNode(' text split', TextType.TEXT)
        ])
