import unittest

from .extract_markdown_links import extract_markdown_links

class ExtractMarkDownLinks(unittest.TestCase):
    def test_extract_md_links(self):
        results = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual(results, [
            ('to boot dev', 'https://www.boot.dev'),
            ('to youtube', 'https://www.youtube.com/@bootdotdev')
        ])