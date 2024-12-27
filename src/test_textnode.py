import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    # Test equality of two identical TextNode instances.
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    # Test the string representation of a TextNode instance.
    def test_repr(self):
        node = TextNode("Sample text", TextType.LINK, "https://example.com")
        expected_repr = "TextNode(Sample text, link, https://example.com)"
        self.assertEqual(repr(node), expected_repr)

    # Test that the url property is correctly set and defaulted.
    def test_url(self):
        # Test with url provided
        node_with_url = TextNode("Sample text", TextType.IMAGE, "https://example.com")
        self.assertEqual(node_with_url.url, "https://example.com")

        # Test with url omitted
        node_without_url = TextNode("Sample text", TextType.IMAGE)
        self.assertIsNone(node_without_url.url)
    
    # Test inequality between different TextNode instances.
    def test_inequality(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()