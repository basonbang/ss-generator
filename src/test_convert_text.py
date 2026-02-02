import unittest 

from textnode import TextNode, TextType 
from convert_text import split_nodes_delimiter

class TestConvertText(unittest.TestCase):
    def test_split_nodes_delimiter_simple(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_nodes = [
            TextNode("This is text with a ", TextType.PLAIN_TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.PLAIN_TEXT)
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_no_delimiter(self):
        node = TextNode("Plain text with no delimiters", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_nodes = [
            TextNode("Plain text with no delimiters", TextType.PLAIN_TEXT)
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_bold_text(self):
        node = TextNode("**This is bold text** and normal text", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)

        expected_nodes = [
            TextNode("This is bold text", TextType.BOLD_TEXT),
            TextNode(" and normal text", TextType.PLAIN_TEXT)
        ]

        self.assertEqual(new_nodes, expected_nodes)
    
    def test_split_nodes_delimiter_bold_text_single_word(self):
        node = TextNode("**Bold**", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)

        expected_nodes = [
            TextNode("Bold", TextType.BOLD_TEXT)
        ]

        self.assertEqual(new_nodes, expected_nodes)
    
    def test_split_nodes_delimiter_unmatched_delimiter_raises(self):
        node = TextNode("This is invalid **Markdown", TextType.PLAIN_TEXT)

        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertIn("Unmatched delimiter '**' found in text", str(context.exception))