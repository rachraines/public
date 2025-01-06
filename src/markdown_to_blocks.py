from textnode import TextNode, TextType

def markdown_to_blocks(markdown):
    blocks = [p.strip() for p in markdown.split("\n\n") if p.strip()]
    
    return blocks