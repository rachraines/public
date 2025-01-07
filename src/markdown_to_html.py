from markdown_to_blocks import markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode
import re

def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == "code":
            tag = "code"
            content = block
        elif block_type == "ordered_list":
            tag = "ol"
            content = block
        elif block_type == "heading":
            match = re.match(r"^(#{1,6} (.+)", block)
            if match:
                num_hashes = len(match.group(1)) # finds number of # chars
                tag = f"h{num_hashes}" # creates appropriate header tag
                content = match.group(2)
        elif block_type == "paragraph":
            tag = "p"
            content = block
        elif block_type == "quote":
            tag = "q"
            content = block
        elif block_type == "unordered_list":
            tag = "ul"
            content = block
        else:
            continue # skip unknown block types
        htmlnode = HTMLNode(tag, content)
        html_nodes.append(htmlnode)

