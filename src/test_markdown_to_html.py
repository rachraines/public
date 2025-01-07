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

    def test_heading(self):
        markdown = "# This is a heading"
        html_node = markdown_to_html(markdown)
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="h1", children=[HTMLNode(tag=None, value="This is a heading")])
        ])
        self.assertEqual(html_node, expected)

    def test_ordered_list(self):
        markdown = """1. First item
2. Second item"""
        html_node = markdown_to_html(markdown)
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="ol", children=[
                HTMLNode(tag="li", children=[HTMLNode(tag=None, value="First item")]),
                HTMLNode(tag="li", children=[HTMLNode(tag=None, value="Second item")])
            ])
        ])
        print(f"Actual HTMLNode children: {[child.tag for child in html_node.children]}")
        print(f"Expected HTMLNode children: {[child.tag for child in expected.children]}")
        print(f"Actual HTMLNode: tag={html_node.tag}, value={html_node.value}, props={html_node.props}, children={html_node.children}")
        print(f"Expected HTMLNode: tag={expected.tag}, value={expected.value}, props={expected.props}, children={expected.children}")
        #for child in html_node.children:
            #print(f"Actual child: tag={child.tag}, value={child.value}, props={child.props}")

        self.assertEqual(html_node, expected)