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
        self.assertEqual(block_to_blocktype("# This is a header"), BlockType.HEADER)
        self.assertEqual(block_to_blocktype("## This is a header"), BlockType.HEADER)
        self.assertEqual(block_to_blocktype("### This is a header"), BlockType.HEADER)
    
    def test_block_to_blocktype_code(self):
        self.assertEqual(block_to_blocktype("```\nThis is code\n```"), BlockType.CODE)
    
    def test_block_to_blocktype_quote(self):
        self.assertEqual(block_to_blocktype("> This is a quote"), BlockType.QUOTE)

    def test_block_to_blocktype_unordered_list(self):
        self.assertEqual(block_to_blocktype("- This is an unordered list item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_blocktype("- Item1\n- Item2\n - Item3"), BlockType.UNORDERED_LIST)
    
    def test_block_to_blocktype_ordered_list(self):
        self.assertEqual(block_to_blocktype("1. This is an ordered list item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_blocktype("1. Item1\n2. Item2\n3. Item3"), BlockType.ORDERED_LIST)

if __name__ == "__main__":
    unittest.main()