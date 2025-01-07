import unittest

from markdown_to_html import markdown_to_html, text_to_children
from htmlnode import HTMLNode

class Markdown_to_HTML(unittest.TestCase):

    def test_paragraph(self):
        markdown = "This is a simple paragraph."
        html_node = markdown_to_html(markdown)
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="p", children=[HTMLNode(tag=None, value="This is a simple paragraph.")])
        ])
        self.assertEqual(html_node, expected)