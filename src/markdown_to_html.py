from markdown_to_blocks import markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode
from text_to_html import text_node_to_html
from text_to_textnodes import text_to_textnodes
import re

def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = None
        
        if block_type == "code":
            code_node = HTMLNode(tag="code", children=[HTMLNode(tag=None, value=block)])
            html_node = HTMLNode(tag="pre", children=[code_node])

        elif block_type == "ordered_list":
            items = block.splitlines()
            list_children = [HTMLNode(tag="li", children=text_to_children(item.strip())) for item in items]
            html_node = HTMLNode(tag="ol", children=list_children)
        
        elif block_type == "heading":
            match = re.match(r"^(#{1,6} (.+)", block)
            if match:
                num_hashes = len(match.group(1)) # finds number of # chars
                tag = f"h{num_hashes}" # creates appropriate header tag
                content = match.group(2).strip()
                html_node = HTMLNode(tag=tag, children=text_to_children(content))
        
        elif block_type == "paragraph":
            html_node = HTMLNode(tag="p", children=text_to_children(block))
        
        elif block_type == "quote":
            content = block.lstrip("> ").strip()
            html_node = HTMLNode(tag="blockquote", children=text_to_children(content))
        
        elif block_type == "unordered_list":
            items = block.splitlines()
            list_children = [HTMLNode(tag="li", children=text_to_children(item.strip())) for item in items]
            html_node = HTMLNode(tag="ul", children=list_children)
        
        else:
            continue # skip unknown block types
        
        if html_node:
            children.append(html_node)
    
    return HTMLNode(tag="div", children=children)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = [text_node_to_html(node) for node in text_nodes]
    return children