import unittest

from .block_to_block_type import block_to_block_type

class TestBlockToBlock(unittest.TestCase):
    def test_heading(self):
        for i in range(1,7):
            heading = f"{'#' * i} Heading"
            result = block_to_block_type(heading)
            self.assertEqual(result, 'Heading')
    
    def test_code(self):
        result = block_to_block_type('```code block here```')
        self.assertEqual(result, 'Code')
    
    def test_quote(self):
        result = block_to_block_type('> Quote block here')
        self.assertEqual(result, 'Quote')
    
    def test_unordered_list(self):
        result = block_to_block_type('* list items')
        self.assertEqual(result, 'Unordered List')

        result = block_to_block_type('- list items')
        self.assertEqual(result, 'Unordered List')
    
    def test_ordered_list(self):
        for i in range(99):
            result = block_to_block_type(f"{i}. List Items")
            self.assertEqual(result, 'Ordered List')
    
    def test_paragraph(self):
        result = block_to_block_type('Lots of text here')
        self.assertEqual(result, 'Paragraph')