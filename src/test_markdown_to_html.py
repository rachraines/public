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
        self.assertEqual(html_node, expected)

    def test_quote(self):
        markdown = "> This is a quote"
        html_node = markdown_to_html(markdown)
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="blockquote", children=[HTMLNode(tag=None, value="This is a quote")])
        ])
        self.assertEqual(html_node, expected)

    def test_code_block(self):
        markdown = """```
    def hello_world():
        print("Hello, World!")
    ```"""
        html_node = markdown_to_html(markdown)

        # Create expected HTMLNode with the exact indentation preserved
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="pre", children=[
                HTMLNode(tag="code", children=[
                    HTMLNode(tag=None, value='def hello_world():\n    print("Hello, World!")', props=None)  # Indentation is preserved
                ], props=None)
            ], props=None)
        ], props=None)

        # Function to normalize values for comparison
        def normalize_value(value):
            if value is None:
                return ""
            return "\n".join([line.strip() for line in value.strip().splitlines()])

        # Recursively compare HTML nodes
        def compare_html_nodes(node1, node2):
            if node1.tag != node2.tag:
                print(f"Different tags: {node1.tag} != {node2.tag}")
            if normalize_value(node1.value) != normalize_value(node2.value):
                print(f"Different values: {normalize_value(node1.value)} != {normalize_value(node2.value)}")
            if len(node1.children) != len(node2.children):
                print(f"Different number of children: {len(node1.children)} != {len(node2.children)}")
            for c1, c2 in zip(node1.children, node2.children):
                compare_html_nodes(c1, c2)  # Recursively compare children
            if node1.props != node2.props:
                print(f"Different props: {node1.props} != {node2.props}")
            
            return (node1.tag == node2.tag and
                    normalize_value(node1.value) == normalize_value(node2.value) and
                    len(node1.children) == len(node2.children) and
                    all(compare_html_nodes(c1, c2) for c1, c2 in zip(node1.children, node2.children)) and
                    (node1.props == node2.props or node1.props is None and node2.props is None))  # Allow props=None to match

        result = compare_html_nodes(html_node, expected)
        self.assertTrue(result)

    def test_empty_input(self):
        markdown = ""
        html_node = markdown_to_html(markdown)
        expected = HTMLNode(tag="div", children=[])
        self.assertEqual(html_node, expected)

    def test_unordered_list(self):
        markdown = """- First item
    - Second item"""
        html_node = markdown_to_html(markdown)
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="ul", children=[
                HTMLNode(tag="li", children=[HTMLNode(tag=None, value="First item")]),
                HTMLNode(tag="li", children=[HTMLNode(tag=None, value="Second item")])
            ])
        ])
        self.assertEqual(html_node, expected)

    def test_multiple_paragraphs(self):
        markdown = """This is the first paragraph.

    This is the second paragraph."""
        
        html_node = markdown_to_html(markdown)
        
        expected = HTMLNode(tag="div", children=[
            HTMLNode(tag="p", children=[HTMLNode(tag=None, value="This is the first paragraph.")], props=None),
            HTMLNode(tag="p", children=[HTMLNode(tag=None, value="This is the second paragraph.")], props=None)
        ], props=None)
        
        self.assertEqual(html_node, expected)


