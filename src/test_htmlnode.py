import unittest 

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_div_with_props(self):
        node = LeafNode("div", "Content", {"class": "container", "id": "main"})

        self.assertEqual(node.to_html(), '<div class="container" id="main">Content</div>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")
    
    def test_leaf_to_html_empty_value_raises(self):
        node = LeafNode("code", None)
        self.assertRaises(ValueError, node.to_html)

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node_1 = LeafNode("li", "Item 1")
        child_node_2 = LeafNode("li", "Item 2")
        child_node_3 = LeafNode("li", "Item 3")
        parent_node = ParentNode("ul", [child_node_1, child_node_2, child_node_3])

        self.assertEqual(
            parent_node.to_html(),
            "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>"
        )
    
    def test_to_html_parent_no_tag_raises(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])

        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_parent_no_children_raises(self):
        parent_node = ParentNode("div", [])

        self.assertRaises(ValueError, parent_node.to_html)

    