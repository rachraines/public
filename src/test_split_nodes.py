import unittest
from split_nodes import *

class Test_Split_Nodes(unittest.TestCase):
    # Orignial non-text node should be returned as a list
    def test_NonText_Nodes(self):
        old_node = [TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.IMAGE,
)]
        new_node = split_nodes_images(old_node)
        expected_output = old_node
        self.assertEqual(new_node, expected_output)

    def test_multiple_links(self):
        old_node = [TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)]
        new_node = split_nodes_links(old_node)
        expected_output =  [
        TextNode("This is text with a link ", TextType.TEXT),
        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        TextNode(" and ", TextType.TEXT),
        TextNode(
         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
     ),
 ]
        self.assertEqual(new_node, expected_output)

    def test_multiple_images(self):
        old_node = [TextNode(
    "This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)]
        new_node = split_nodes_images(old_node)
        expected_output =  [
        TextNode("This is text with an image ", TextType.TEXT),
        TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
        TextNode(" and ", TextType.TEXT),
        TextNode(
         "to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"
     ),
 ]
        self.assertEqual(new_node, expected_output)

    def test_empty_input(self):
        old_node = []
        new_node_links = split_nodes_links(old_node)
        new_node_images = split_nodes_images(old_node)
        self.assertEqual(new_node_links, [])
        self.assertEqual(new_node_images, [])

    def test_no_matches(self):
        old_node = [TextNode("This is just plain text with no links or images.", TextType.TEXT)]
        new_node_links = split_nodes_links(old_node)
        new_node_images = split_nodes_images(old_node)
        self.assertEqual(new_node_links, old_node)
        self.assertEqual(new_node_images, old_node)

    def test_consecutive_links(self):
        old_node = [TextNode("[Link1](https://link1.com)[Link2](https://link2.com)", TextType.TEXT)]
        new_node = split_nodes_links(old_node)
        expected_output = [
            TextNode("Link1", TextType.LINK, "https://link1.com"),
            TextNode("Link2", TextType.LINK, "https://link2.com"),
        ]
        self.assertEqual(new_node, expected_output)

    def test_consecutive_images(self):
        old_node = [TextNode("![Image1](https://image1.com)![Image2](https://image2.com)", TextType.TEXT)]
        new_node = split_nodes_images(old_node)
        expected_output = [
            TextNode("Image1", TextType.IMAGE, "https://image1.com"),
            TextNode("Image2", TextType.IMAGE, "https://image2.com"),
        ]
        self.assertEqual(new_node, expected_output)

    def test_links_and_images(self):
        old_node = [TextNode(
            "Here is a [link](https://example.com) and an image ![Alt](https://example.com/img).",
            TextType.TEXT,
        )]
        new_node_links = split_nodes_links(old_node)
        new_node_images = split_nodes_images(new_node_links)
        expected_output = [
            TextNode("Here is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and an image ", TextType.TEXT),
            TextNode("Alt", TextType.IMAGE, "https://example.com/img"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(new_node_images, expected_output)

    def test_edge_case_start_end(self):
        old_node = [TextNode("[Start](https://start.com) middle ![End](https://end.com)", TextType.TEXT)]
        new_node_links = split_nodes_links(old_node)
        new_node_images = split_nodes_images(new_node_links)
        expected_output = [
            TextNode("Start", TextType.LINK, "https://start.com"),
            TextNode(" middle ", TextType.TEXT),
            TextNode("End", TextType.IMAGE, "https://end.com"),
        ]
        self.assertEqual(new_node_images, expected_output)




