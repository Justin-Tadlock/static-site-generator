import unittest

from .extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title('# Hello'), 'Hello')

    def test_raise_exception(self):
        try:
            extract_title('Hello')
        except ValueError as e:
            self.assertRaises(ValueError)
            self.assertEqual(e.__str__(), 'Invalid title markdown')