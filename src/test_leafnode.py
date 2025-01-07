import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    # tests LeafNode instance with initialized values
    def test_initialization(self):
        node = LeafNode(tag="p", value="paragraph text", props={"href": "https://google.com"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "paragraph text")
        self.assertEqual(node.props, {"href": "https://google.com"})
        self.assertEqual(node.children, [])

    # tests LeafNode instance with default values
    def test_initialization_defaults(self):
        with self.assertRaises(ValueError):
            LeafNode()

    # tests to_html method
    def test_to_html(self):
        node = LeafNode("a", "Click me!", props={"href": "https://google.com"})
        expected_string = "<a href='https://google.com'>Click me!</a>"
        self.assertEqual(node.to_html(), expected_string)

    # tests to_html with no props
    def test_to_html_no_props(self):
        node = LeafNode("a", "Click me!")
        expected_string = "<a>Click me!</a>"
        self.assertEqual(node.to_html(), expected_string)

    # tests to_html with no tag
    def test_to_html_no_tag(self):
        node = LeafNode(value="Click me!")
        self.assertEqual(node.to_html(), "Click me!")

    # test to_html with no value
    def test_to_html_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="p")
