import unittest
from markdown_to_blocks import markdown_to_blocks
from textnode import TextNode, TextType

class Test_Markdown_to_Blocks(unittest.TestCase):
    def test_Markdown_to_Blocks(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        blocks = markdown_to_blocks(text)
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        
        self.assertEqual(blocks, expected_blocks)
    