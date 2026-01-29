import unittest 

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_creation_no_children(self):
        node = HTMLNode(tag="p", value="paragraph tag", children=[], props={"class": "text-center"})

        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "paragraph tag")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "text-center"})
    
    def test_htmlnode_creation_with_children(self):
        child_1 = HTMLNode(tag="b", value="bold text")
        child_2 = HTMLNode(tag="i", value="italic text")

        node = HTMLNode(tag="p", value="paragraph tag", children=[child_1, child_2], props={"id": "intro"})

        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "paragraph tag")
        self.assertEqual(node.children, [child_1, child_2])
        self.assertEqual(node.props, {"id": "intro"})

    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="link", props={"href": "https://boot.dev", "target": "_blank"})
        test_string = node.props_to_html()

        self.assertEqual(test_string, ' href="https://boot.dev" target="_blank"')