import unittest
from markdown_to_blocks import markdown_to_blocks, block_to_block_type
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

class Test_Block_to_Block_Type(unittest.TestCase):
    def test_heading(self):
        block = "# This is a heading."
        block_type = block_to_block_type(block)
        expected_blocktype = "heading"
        self.assertEqual(block_type, expected_blocktype)

    def test_additional_headings(self):
        block = "### This is also a heading."
        block_type = block_to_block_type(block)
        expected_blocktype = "heading"
        self.assertEqual(block_type, expected_blocktype)

    def test_heading_no_space(self):
        block = "#####This is not a heading becuase it has no space."
        block_type = block_to_block_type(block)
        expected_blocktype = "paragraph"
        self.assertEqual(block_type, expected_blocktype)

    def test_code(self):
        block = "```This is code.```"
        block_type = block_to_block_type(block)
        expected_blocktype = "code"
        self.assertEqual(block_type, expected_blocktype)

    def test_unclosed_code(self):
        block = "```This is not code."
        block_type = block_to_block_type(block)
        expected_blocktype = "paragraph"
        self.assertEqual(block_type, expected_blocktype)

    def test_quote(self):
        block = """>This is
>a quote
>yup."""
        block_type = block_to_block_type(block)
        expected_blocktype = "quote"
        self.assertEqual(block_type, expected_blocktype)

    def test_almost_quote(self):
        block = """>This is
a quote
>yup."""
        block_type = block_to_block_type(block)
        expected_blocktype = "paragraph"
        self.assertEqual(block_type, expected_blocktype)

    def test_unordered_list_stars(self):
        block = """* This is a list
* item 1
* item 2"""
        block_type = block_to_block_type(block)
        expected_blocktype = "unordered_list"
        self.assertEqual(block_type, expected_blocktype)
    
    def test_unordered_list_dash(self):
        block = """- This is a list
- item 1
- item 2"""
        block_type = block_to_block_type(block)
        expected_blocktype = "unordered_list"
        self.assertEqual(block_type, expected_blocktype)

    def test_ordered_list(self):
        block = """1. This is a list
2. item 1
3. item 2"""
        block_type = block_to_block_type(block)
        expected_blocktype = "ordered_list"
        self.assertEqual(block_type, expected_blocktype)

    def test_ordered_list_incorrect_order(self):
        block = """1. This is a list
3. item 1
4. item 2"""
        block_type = block_to_block_type(block)
        expected_blocktype = "paragraph"
        self.assertEqual(block_type, expected_blocktype)