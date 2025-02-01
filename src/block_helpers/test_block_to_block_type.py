import unittest

from .block_to_block_type import BlockType, block_to_block_type

class TestBlockToBlock(unittest.TestCase):
    def test_heading(self):
        for i in range(1,7):
            heading = f"{'#' * i} Heading"
            result = block_to_block_type(heading)
            self.assertEqual(result, BlockType.HEADING)
    
    def test_code(self):
        result = block_to_block_type('```code block here```')
        self.assertEqual(result, BlockType.CODE)

        result = block_to_block_type('```\ncode block here\n```')
        self.assertEqual(result, BlockType.CODE)
    
    def test_quote(self):
        result = block_to_block_type('> Quote block here')
        self.assertEqual(result, BlockType.QUOTE)
    
    def test_unordered_list(self):
        result = block_to_block_type('* list items')
        self.assertEqual(result, BlockType.U_LIST)

        result = block_to_block_type('- list items')
        self.assertEqual(result, BlockType.U_LIST)
    
    def test_ordered_list(self):
        block_text = ''
        for i in range(1,10):
            block_text += f"{i}. List Item\n"
        block_text = block_text.rstrip('\n')

        result = block_to_block_type(block_text)
        self.assertEqual(result, BlockType.O_LIST)
    
    def test_paragraph(self):
        result = block_to_block_type('Lots of text here')
        self.assertEqual(result, BlockType.PARAGRAPH)