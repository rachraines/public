import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class Test_Text_To_TextNodes(unittest.TestCase):

    def test_text_to_texnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        output_nodes = text_to_textnodes(text)
        expected_nodes = [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
]
        self.assertEqual(output_nodes, expected_nodes)
        
    def test_empty_string(self):
        text = ""
        output_nodes = text_to_textnodes(text)
        expected_nodes = []
        self.assertEqual(output_nodes, expected_nodes)

    def test_basic_text(self):
        text = "This is plain text."
        output_nodes = text_to_textnodes(text)
        expected_nodes = [TextNode("This is plain text.", TextType.TEXT)]
        self.assertEqual(output_nodes, expected_nodes)

    def test_bold_text(self):
        text = "This is **bold** text."
        output_nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(output_nodes, expected_nodes)

    def test_italic_text(self):
        text = "This is *italic* text."
        output_nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(output_nodes, expected_nodes)

    def test_code_text(self):
        text = "This is `code` text."
        output_nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(output_nodes, expected_nodes)

    def test_text_with_images(self):
        text = "This is an ![image](https://example.com/image.jpg)."
        output_nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/image.jpg"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(output_nodes, expected_nodes)

    def test_text_with_links(self):
        text = "Visit [this site](https://example.com)."
        output_nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("Visit ", TextType.TEXT),
            TextNode("this site", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(output_nodes, expected_nodes)

