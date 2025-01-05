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
        text= ""
        output_nodes = text_to_textnodes(text)
        expected_nodes = []
        self.assertEqual(output_nodes, expected_nodes)
