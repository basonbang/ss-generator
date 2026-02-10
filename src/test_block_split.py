import unittest
from block_split import *

class TestBlockSplit(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_with_extra_newlines(self):
        md = """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here",
            ],
        )
    
    def test_block_to_blocktype_header(self):
        self.assertEqual(block_to_blocktype("# This is a header"), BlockType.HEADING)
        self.assertEqual(block_to_blocktype("## This is a header"), BlockType.HEADING)
        self.assertEqual(block_to_blocktype("### This is a header"), BlockType.HEADING)
    
    def test_block_to_blocktype_code(self):
        self.assertEqual(block_to_blocktype("```\nThis is code\n```"), BlockType.CODE)
    
    def test_block_to_blocktype_quote(self):
        self.assertEqual(block_to_blocktype("> This is a quote"), BlockType.QUOTE)

    def test_block_to_blocktype_unordered_list(self):
        self.assertEqual(block_to_blocktype("- This is an unordered list item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_blocktype("- Item1\n- Item2\n- Item3"), BlockType.UNORDERED_LIST)
    
    def test_block_to_blocktype_ordered_list(self):
        self.assertEqual(block_to_blocktype("1. This is an ordered list item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_blocktype("1. Item1\n2. Item2\n3. Item3"), BlockType.ORDERED_LIST)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )
    
    def test_quote(self):
        md = """
> This is a quote
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote</blockquote></div>",
        )
    
    def test_unordered_list(self):
        md = """
- Item 1
- Item 2
- Item 3
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>",
        )   
    
    def test_ordered_list(self):
        md = """
1. Item 1
2. Item 2
3. Item 3
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol></div>",
        )
    
    def test_heading(self):
        md = """# Heading 1

## Heading 2

### Heading 3
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>",
        )

if __name__ == "__main__":
    unittest.main()