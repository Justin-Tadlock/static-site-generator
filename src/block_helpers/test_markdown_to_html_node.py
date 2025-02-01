import unittest

from .markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_basic_html(self):
        markdown = """# Heading 1

This is a paragraph

This is a **bold** paragraph

Not really an *italic* paragraph
"""
        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            '<div><h1>Heading 1</h1><p>This is a paragraph</p><p>This is a <b>bold</b> paragraph</p><p>Not really an <i>italic</i> paragraph</p></div>'
        )
    
    def test_ul_html(self):
        markdown = """## Heading 2

* List 1
* List 2

- List a
- List b
"""
        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            '<div><h2>Heading 2</h2><ul><li>List 1</li><li>List 2</li></ul><ul><li>List a</li><li>List b</li></ul></div>'
        )

    def test_ol_html(self):
        markdown = """### Heading 3

1. List 1
2. List 2
"""
        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            '<div><h3>Heading 3</h3><ol><li>List 1</li><li>List 2</li></ol></div>'
        )

    def test_code_htlm(self):
        markdown = """#### Heading 4

```
const example = () => ('some basic code');
```
"""
        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            "<div><h4>Heading 4</h4><pre><code>const example = () => ('some basic code');</code></pre></div>"
        )

    def test_quote_html(self):
        markdown = """##### Heading 5

> Just an
> every day
> mother quote-ah!
"""
        self.assertEqual(
            markdown_to_html_node(markdown).to_html(),
            '<div><h5>Heading 5</h5><blockquote>Just an every day mother quote-ah!</blockquote></div>'
        )