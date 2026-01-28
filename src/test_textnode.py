import unittest

from textnode import TextNode, TextType 

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text node 1", TextType.PLAIN_TEXT)
        node2 = TextNode("This is text node 1", TextType.PLAIN_TEXT)

        self.assertEqual(node, node2)
    
    def test_neq(self):
        node = TextNode("This is text node 1", TextType.PLAIN_TEXT)
        node2 = TextNode("This is text node 2", TextType.PLAIN_TEXT)

        self.assertNotEqual(node, node2)
    
    def test_neq_different_texttype(self):
        node = TextNode("This is text node 1", TextType.PLAIN_TEXT)
        node2 = TextNode("This is text node 1", TextType.BOLD_TEXT)

        self.assertNotEqual(node, node2)

    def test_neq_different_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://docs.python.org/3/library/unittest.html")
        node2 = TextNode("This is a link", TextType.LINK, "https://www.boot.dev/dashboard")

        self.assertNotEqual(node, node2)        

if __name__ == "__main__":
    unittest.main()