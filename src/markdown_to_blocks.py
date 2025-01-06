from textnode import TextNode, TextType
import re

def markdown_to_blocks(markdown):
    blocks = []
    # strip leading/trailing whitespace for the entire string
    markdown = markdown.strip()

    # split by 2 or more consecutive new lines
    for p in markdown.split("\n\n"):
        # strip each block again
        block = p.strip()
        if block:
            # strip each line in the block, then join them back together
            block_lines = "\n".join([line.strip() for line in block.split("\n")])
            blocks.append(block_lines)
    
    return blocks

def block_to_block_type(block):
    lines = block.splitlines()
    if block.startswith("#"):
        return "heading"
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    elif all(line.startswith(">") for line in lines):
        return "quote"
    elif all(line.startswith(("* ", "- ")) for line in lines):
        return "unordered_list"
    start_number = 0
    for line in lines:
        start_number += 1
        if line.startswith(f"{start_number}. "):
            return "ordered_list"
        
    return "paragraph"