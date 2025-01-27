import unittest

from delimited_slices import get_delimited_slices

class GetDelimitedSlices(unittest.TestCase):
    def test_not_found(self):
        text = 'Testing **bold** Splicing'
        sliced, delim, remainder = get_delimited_slices(text, '`')
        self.assertEqual(sliced, '')
        self.assertEqual(delim, '')
        self.assertEqual(remainder, "Testing **bold** Splicing")

    def test_found_bold(self):
        text = 'Testing **bold** Splicing'
        sliced, delim, remainder = get_delimited_slices(text, '**')
        self.assertEqual(sliced, 'Testing ')
        self.assertEqual(delim, 'bold')
        self.assertEqual(remainder, " Splicing")

    def test_found_italic(self):
        text = 'Testing *italic* Splicing'
        sliced, delim, remainder = get_delimited_slices(text, '*')
        self.assertEqual(sliced, 'Testing ')
        self.assertEqual(delim, 'italic')
        self.assertEqual(remainder, " Splicing")

    def test_found_code(self):
        text = 'Testing `code` Splicing'
        sliced, delim, remainder = get_delimited_slices(text, '`')
        self.assertEqual(sliced, 'Testing ')
        self.assertEqual(delim, 'code')
        self.assertEqual(remainder, " Splicing")

    def text_no_matching_closing_delim(self):
        text = 'Testing `code Splicing'
        sliced, delim, remainder = get_delimited_slices(text, '`')
        self.assertRaises(Exception)