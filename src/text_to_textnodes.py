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
    for delimiter, text_type in [
        ("**", TextType.BOLD),
        ("*", TextType.ITALIC),
        ("`", TextType.CODE)
    ]:
        new_nodes = []
        for node in nodes:
            if node.text_type == TextType.TEXT:
                new_nodes.extend(split_nodes_delimiter([node], delimiter, text_type))
            else:
                new_nodes.append(node)
        nodes = new_nodes

    return nodes

