import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_valid(self):
        # Test with a valid H1 header
        markdown = "# Hello"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello")
    
    def test_extract_title_with_extra_spaces(self):
        # Test with an H1 header with extra spaces before and after the title
        markdown = "#    Hello    "
        result = extract_title(markdown)
        self.assertEqual(result, "Hello")
    
    def test_extract_title_missing_header(self):
        # Test with markdown that does not contain an H1 header
        markdown = "This is not an H1 header"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertTrue("No h1 header found" in str(context.exception))

    def test_extract_title_multiple_hashes(self):
        # Test that only a single '#' is considered for H1
        markdown = "## Not an H1 header"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertTrue("No h1 header found" in str(context.exception))

    def test_extract_title_empty_string(self):
        # Test with an empty string, should not find an H1 header
        markdown = ""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertTrue("No h1 header found" in str(context.exception))

    def test_extract_title_no_header(self):
        # Test when there is no header at all
        markdown = "This is some text without any headers"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertTrue("No h1 header found" in str(context.exception))