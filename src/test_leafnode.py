import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    # tests LeafNode instance with initialized values
    def test_initialization(self):
        node = LeafNode(tag="p", value="paragraph text", props={"href": "https://google.com"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "paragraph text")
        self.assertEqual(node.props, {"href": "https://google.com"})
        self.assertIsNone(node.children)

    # tests LeafNode instance with default values
    def test_initialization_defaults(self):
        node = LeafNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        with self.assertRaises(ValueError):
            LeafNode()

    # tests to_html method
    def test_to_html(self):
        node = LeafNode("a", "Click me!", props={"href": "https://google.com"})
        expected_string = "<a href='https://google.com'>Click me!</a>"
        self.assertEqual(node.to_html(), expected_string)
