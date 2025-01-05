from split_nodes import split_nodes_images, split_nodes_links
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


def text_to_textnodes(text):
    # turns text into a TextNode
    nodes = [TextNode(text, TextType.TEXT)]

    # process images
    nodes = split_nodes_images(nodes)
    # process links
    nodes = split_nodes_links(nodes)

    # process bold, italic, and code
    new_nodes = []
    for node in nodes:
        if node.text_type == TextType.TEXT:
            node = split_nodes_delimiter(node, "**", TextType.BOLD)
            node = split_nodes_delimiter(node, "*", TextType.ITALIC)
            node = split_nodes_delimiter(node, "`", TextType.CODE)
        new_nodes.append(node)

    return new_nodes

