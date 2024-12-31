import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    # tests ParentNode instance with initialized values
    def test_initialization(self):
        child1 = LeafNode("b", "Bold text")
        child2 = LeafNode(None, "Normal text")
        child3 = LeafNode("i", "italic text")
        node = ParentNode(tag="p", children=[child1, child2, child3], props={"href": "https://google.com"})

        self.assertEqual(node.tag, "p")
        self.assertEqual(node.children, [child1, child2, child3])
        self.assertEqual(node.props, {"href": "https://google.com"})
        self.assertIsNone(node.value)

    # tests ParentNode instance with missing children
    def test_missing_children(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="p", children=None)
    
    # tests ParentNode instance with empty children
    def test_empty_children(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="p", children=[])
    
    # tests ParentNode with missing tag
    def test_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[LeafNode("b", "Bold text")])

    # tests to_html method
    def test_to_html(self):
        child1 = LeafNode("b", "Bold text")
        child2 = LeafNode(None, "Normal text")
        child3 = LeafNode("i", "italic text")
        node = ParentNode(tag="p", children=[child1, child2, child3], props={"href": "https://google.com"})
        expected_string = "<p href='https://google.com'><b>Bold text</b>Normal text<i>italic text</i></p>"
        self.assertEqual(node.to_html(), expected_string)

    # tests nested parent node
    def test_nested_parent_node(self):
        child1 = LeafNode("b", "Bold text")
        child2 = ParentNode(tag="a", children=[LeafNode("i", "italic text")])
        node = ParentNode(tag="p", children=[child1, child2])
        expected_string = "<p><b>Bold text</b><a><i>italic text</i></a></p>"
        self.assertEqual(node.to_html(), expected_string)

    # tests to_html with no props
    def test_to_html_no_props(self):
        child1 = LeafNode("b", "Bold text")
        child2 = LeafNode(None, "Normal text")
        child3 = LeafNode("i", "italic text")
        node = ParentNode(tag="p", children=[child1, child2, child3], props=None)
        expected_string = "<p><b>Bold text</b>Normal text<i>italic text</i></p>"
        self.assertEqual(node.to_html(), expected_string)

    # tests to_html with no tag
    def test_to_html_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[LeafNode("b", "Bold text")])

   # test to_html with no children
    def test_to_html_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="p", children=None)


