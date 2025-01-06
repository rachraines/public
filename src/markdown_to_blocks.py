from textnode import TextNode, TextType

def markdown_to_blocks(markdown):
    lines = markdown.splitlines()
    nodes = []
    for line in lines:
        if line == "":
            continue
        nodes.append(TextNode(line, TextType.TEXT))
    new_nodes = nodes
    return new_nodes