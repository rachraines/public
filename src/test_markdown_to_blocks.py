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
    
    def test_no_input(self):
        text = ""
        blocks = markdown_to_blocks(text)
        expected_blocks = []
        
        self.assertEqual(blocks, expected_blocks)

    def test_single_block_input(self):
        text = "# This is a heading"
        blocks = markdown_to_blocks(text)
        expected_blocks = ["# This is a heading"]

        self.assertEqual(blocks, expected_blocks)

    def test_consecutive_new_lines(self):
        text = """# Heading

This is the first paragraph.


This is the second paragraph."""
        blocks = markdown_to_blocks(text)
        expected_blocks = [
            "# Heading",
            "This is the first paragraph.",
            "This is the second paragraph."
        ]
        self.assertEqual(blocks, expected_blocks)

    def test_leading_trailing_whitespace(self):
        text = """  
        # Heading with spaces

        This is a paragraph with leading and trailing spaces.   
        """
        blocks = markdown_to_blocks(text)
        expected_blocks = [
            "# Heading with spaces",
            "This is a paragraph with leading and trailing spaces."
        ]
        self.assertEqual(blocks, expected_blocks)

    def test_single_list_block(self):
        text = """* Item 1
        * Item 2
        * Item 3"""
        blocks = markdown_to_blocks(text)
        expected_blocks = [
                "* Item 1\n* Item 2\n* Item 3"
            ]
        self.assertEqual(blocks, expected_blocks)

        

    