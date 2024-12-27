import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    # tests HTMLNode instance with initialized values
    def test_initialization(self):
        node = HTMLNode(tag="p", value="paragraph text", children=["b","i"], props={"href": "https://google.com"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "paragraph text")
        self.assertEqual(node.children, ["b", "i"])
        self.assertEqual(node.props, {"href": "https://google.com"})

    # tests HTMLNode instance with default values
    def test_initialization_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    # tests props_to_html method
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        expected_props_string = "href= https://google.com target= _blank"
        self.assertEqual(node.props_to_html(), expected_props_string)

    # tests __repr__ method
    def test__repr__(self):
        node = HTMLNode(tag="p", value="paragraph text", children=["b","i"], props={"href": "https://google.com"})
        expected_repr = (
            "HTMLNode(tag=p, value=paragraph text, children=[b, i], props={ href:https://google.com})"
        )
        self.assertEqual(repr(node),expected_repr)