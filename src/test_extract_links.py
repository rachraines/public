import unittest

from extract_links import *

class Test_extract_links(unittest.TestCase):
    
    # Tests for extract_markdown_images
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = extract_markdown_images(text)
        expected_list = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extracted_images, expected_list)

    def test_multiple_images(self):
        text = "![Alt 1](image1.png) and ![Alt 2](image2.jpg)"
        extracted_images = extract_markdown_images(text)
        expected_list = [("Alt 1", "image1.png"), ("Alt 2", "image2.jpg")]
        self.assertEqual(extracted_images, expected_list)

    def test_no_image(self):
        text = "This text has no images."
        extracted_images = extract_markdown_images(text)
        expected_list = []
        self.assertEqual(extracted_images, expected_list)

    def test_missing_image_link(self):
        text = "![Alt text only]"
        extracted_images = extract_markdown_images(text)
        expected_list = []
        self.assertEqual(extracted_images, expected_list)

    def test_missing_parentheses(self):
        text = "![Alt text](missing parentheses"
        extracted_images = extract_markdown_images(text)
        expected_list = []
        self.assertEqual(extracted_images, expected_list)

    def test_alt_text_special_chars(self):
        text = "![Alt text with sepcial chars *&^%$#](image.png)"
        extracted_images = extract_markdown_images(text)
        expected_list = [("Alt text with sepcial chars *&^%$#", "image.png")]
        self.assertEqual(extracted_images, expected_list)

    def test_empty_alt_text(self):
        text = "![](image.png)"
        extracted_images = extract_markdown_images(text)
        expected_list = [("", "image.png")]
        self.assertEqual(extracted_images, expected_list)

    # Tests for extract_markdown_links
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links = extract_markdown_links(text)
        expected_list = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extracted_links, expected_list)

    def test_no_links(self):
        text = "This is text with no links"
        extracted_links = extract_markdown_links(text)
        expected_list = []
        self.assertEqual(extracted_links, expected_list)

    def test_missing_links_parentheses(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev"
        extracted_links = extract_markdown_links(text)
        expected_list = []
        self.assertEqual(extracted_links, expected_list)

    def test_empty_link_text(self):
        text = "This is text with a link [](https://www.boot.dev)"
        extracted_links = extract_markdown_links(text)
        expected_list = [("", "https://www.boot.dev")]
        self.assertEqual(extracted_links, expected_list)
    