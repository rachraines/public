import unittest
from text_to_html import *
from parentnode import ParentNode

class Test_Text_To_HTML(unittest.TestCase):
    # tests text_node_to_html with invalid TextType.
    def test_Invalid_TextType(self):
        text_node = TextNode(text="hello", text_type="plain")
        with self.assertRaises(ValueError):
            text_node_to_html(text_node)
            
    # tests text_node_to_html with "text" TextType.
    def test_Text_TextType(self):
        text_node = TextNode(text="hello", text_type=TextType.TEXT)
        leaf_node = text_node_to_html(text_node)
        expected_html = "hello"
        self.assertEqual(leaf_node.to_html(), expected_html)

    # tests text_node_to_html with "bold" TextType.
    def test_Bold_TextType(self):
        text_node = TextNode(text="hello", text_type=TextType.BOLD)
        leaf_node = text_node_to_html(text_node)
        expected_html = "<b>hello</b>"
        self.assertEqual(leaf_node.to_html(), expected_html)

    # tests text_node_to_html with "italic" TextType.
    def test_Italic_TextType(self):
        text_node = TextNode(text="hello", text_type=TextType.ITALIC)
        leaf_node = text_node_to_html(text_node)
        expected_html = "<i>hello</i>"
        self.assertEqual(leaf_node.to_html(), expected_html)

    # tests text_node_to_html with "code" TextType.
    def test_Code_TextType(self):
        text_node = TextNode(text="hello", text_type=TextType.CODE)
        leaf_node = text_node_to_html(text_node)
        expected_html = "<code>hello</code>"
        self.assertEqual(leaf_node.to_html(), expected_html)

    # tests text_node_to_html with "link" TextType.
    def test_Link_TextType(self):
        text_node = TextNode(text="hello", text_type=TextType.LINK, url="https://www.google.com")
        leaf_node = text_node_to_html(text_node)
        expected_html = "<a href='https://www.google.com'>hello</a>"
        self.assertEqual(leaf_node.to_html(), expected_html)

    # tests text_node_to_html with "image" TextType and alt-text.
    def test_Image_TextType(self):
        text_node = TextNode(text="hello", text_type=TextType.IMAGE, url="https://www.google.com")
        leaf_node = text_node_to_html(text_node)
        expected_html = "<img src='https://www.google.com' alt='hello'></img>"
        self.assertEqual(leaf_node.to_html(), expected_html)

    # tests text_node_to_html with "image" TextType and default alt-text.
    def test_Image_TextType(self):
        text_node = TextNode(text="", text_type=TextType.IMAGE, url="https://www.google.com")
        leaf_node = text_node_to_html(text_node)
        expected_html = "<img src='https://www.google.com' alt='alt text'></img>"
        self.assertEqual(leaf_node.to_html(), expected_html)

    # tests text_node_to_html with "link" TextType and missing url.
    def test_Link_NoURL_TextType(self):
        text_node = TextNode(text="hello", text_type=TextType.LINK, url=None)
        with self.assertRaises(ValueError):
            text_node_to_html(text_node)

    # tests text_node_to_html with "image" TextType and missing url.
    def test_Image_NoURL_TextType(self):
        text_node = TextNode(text="hello", text_type=TextType.IMAGE, url=None)
        with self.assertRaises(ValueError):
            text_node_to_html(text_node)

    # tests text_node_to_html with empty text for "text" TextType
    def test_Empty_Text_TextType(self):
        text_node = TextNode(text="", text_type=TextType.TEXT)
        leaf_node = text_node_to_html(text_node)
        expected_html = ""
        self.assertEqual(leaf_node.to_html(), expected_html)

    # tests text_node_to_html with None text for "text" TextType
    def test_None_Text_TextType(self):
        text_node = TextNode(text=None, text_type=TextType.TEXT)
        with self.assertRaises(ValueError):
            text_node_to_html(text_node)

    # tests recursive nested nodes
    def test_Nested_TextNodes(self):
        bold_text_node = TextNode(text="bold", text_type=TextType.BOLD)
        italic_text_node = TextNode(text="italic", text_type=TextType.ITALIC)

        bold_leaf_node = text_node_to_html(bold_text_node)
        italic_leaf_node = text_node_to_html(italic_text_node)

        parent_node = ParentNode(tag="p", children=[bold_leaf_node, italic_leaf_node])
        expected_html = "<p><b>bold</b><i>italic</i></p>"
        self.assertEqual(parent_node.to_html(), expected_html)


