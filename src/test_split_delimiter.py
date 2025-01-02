import unittest
from split_delimiter import *
from leafnode import LeafNode

class Test_Split_Delimiter(unittest.TestCase):
    # Orignial non-text node should be returned as a list
    def test_NonText_Nodes(self):
        old_node = [TextNode("*hello* there", TextType.CODE)]
        new_node = split_nodes_delimiter(old_node, "*", TextType.CODE)
        expected_output = old_node
        self.assertEqual(new_node, expected_output)

    # Raise error if incorrect delimiter given
    def test_Incorrect_Delimiter(self):
        old_node = [TextNode("*hello* there", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_node, "/", TextType.ITALIC)

    # Split text at *
    def test_Bold_Delimiter(self):
        old_node = [TextNode("*hello* there", TextType.TEXT)]
        new_node = split_nodes_delimiter(old_node, "*", TextType.BOLD)
        expected_output = [
            TextNode("hello", TextType.BOLD),
            TextNode(" there", TextType.TEXT)
        ]
        self.assertEqual(new_node, expected_output)

    # Split text at **
    def test_Italic_Delimiter(self):
        old_node = [TextNode("hello **there**", TextType.TEXT)]
        new_node = split_nodes_delimiter(old_node, "**", TextType.ITALIC)
        expected_output = [
            TextNode("hello ", TextType.TEXT),
            TextNode("there", TextType.ITALIC)
        ]
        self.assertEqual(new_node, expected_output)

    # Split text at `
    def test_Code_Delimiter(self):
        old_node = [TextNode("hello `there` mate", TextType.TEXT)]
        new_node = split_nodes_delimiter(old_node, "`", TextType.CODE)
        expected_output = [
            TextNode("hello ", TextType.TEXT),
            TextNode("there", TextType.CODE),
            TextNode(" mate", TextType.TEXT)
        ]
        self.assertEqual(new_node, expected_output)

    # Test with multiple nodes and delimiters
    def test_multiple_casess(self):
        old_node = [TextNode("**bold** text", TextType.TEXT), TextNode("*italic* text",
                    TextType.TEXT), TextNode("`code` text", TextType.TEXT)]
        new_node_bold = split_nodes_delimiter(old_node, "**", TextType.BOLD)
        new_node_italic = split_nodes_delimiter(new_node_bold, "*", TextType.ITALIC)
        new_node_code = split_nodes_delimiter(new_node_italic, "`", TextType.CODE)
        expected_output = [
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(new_node_code, expected_output)

    # Test multiple delimiters in one node
    def test_multiple_delimiters(self):
        old_node = [TextNode("**bold** and *italic* and `code` all together", TextType.TEXT)]
        new_node = split_nodes_delimiter(old_node, "**", TextType.BOLD)
        new_node = split_nodes_delimiter(new_node, "*", TextType.ITALIC)
        new_node = split_nodes_delimiter(new_node, "`", TextType.CODE)
        expected_output = [
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" all together", TextType.TEXT)
        ]
        self.assertEqual(new_node, expected_output)

        # Test unclosed delimiter
        def test_unclosed_delimiter(self):
            old_node = [TextNode("**bold and *italic* and `code` all together", TextType.TEXT)]
            with self.assertraises(ValueError):
                split_nodes_delimiter(old_node, "**", TextType.BOLD)
