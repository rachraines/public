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
    if re.match(r"^#{1,6} .+", block):
        return "heading"
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    elif all(line.startswith(">") for line in lines):
        return "quote"
    elif all(line.startswith(("* ", "- ")) for line in lines):
        return "unordered_list"
    start_number = 1
    for line in lines:
        match = re.match(r"^(\d+)\. ", line)
        if match:
            number = int(match.group(1))
            if number != start_number:
                return "paragraph"
            start_number += 1
        else: 
            return "paragraph"
        
    return "ordered_list"