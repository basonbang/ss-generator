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

    def test_plain_text(self):
        node = TextNode("This is plain text", TextType.PLAIN_TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is plain text")

    def test_bold_text(self):
        node = TextNode("This is bold text", TextType.BOLD_TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_italic_text(self):
        node = TextNode("This is italic text", TextType.ITALIC_TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")

    def test_code_text(self):
        node = TextNode("print('Hello, world!')", TextType.CODE)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('Hello, world!')")

    def test_link_text(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        html_node = node.text_node_to_html_node()

        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Boot.dev")   
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})
    
    def test_image_text(self):
        node = TextNode("Boot.dev Logo", TextType.IMAGE, "https://boot.dev/logo.png")
        html_node = node.text_node_to_html_node()

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")   
        self.assertEqual(html_node.props, {"src": "https://boot.dev/logo.png", "alt": "Boot.dev Logo"})

if __name__ == "__main__":
    unittest.main()