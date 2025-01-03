import unittest

from extract_links import *

class Test_extract_links(unittest.TestCase):
    # tests HTMLNode instance with initialized values
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_links = extract_markdown_images(text)
        expected_list = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extracted_links, expected_list)