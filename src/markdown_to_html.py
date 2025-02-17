from markdown_to_blocks import markdown_to_blocks, block_to_block_type
from parentnode import ParentNode
from leafnode import LeafNode
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
            block_content = block.strip("`").strip()
            code_node = LeafNode(tag="code", value=block_content)
            html_node = ParentNode(tag="pre", children=[code_node], props=None)

        elif block_type == "ordered_list":
            items = block.splitlines()
            list_children = []

            for item in items:
                match = re.match(r"^(\d+)\.\s*(.*)", item.strip())
                if match:
                    number = match.group(1)  # This captures the number (e.g., "1", "2")
                    text = match.group(2)  # This captures the item content (e.g., "First item")

                    # Create an li node with the item content as value
                    li_node = ParentNode(tag="li", children=text_to_children(text), props=None)
                    list_children.append(li_node)
            
            html_node = ParentNode(tag="ol", children=list_children)
        
        elif block_type == "heading":
            match = re.match(r"^(#{1,6})\s*(.+)", block)
            if match:
                num_hashes = len(match.group(1)) # finds number of # chars
                tag = f"h{num_hashes}" # creates appropriate header tag
                content = match.group(2).strip()
                html_node = ParentNode(tag=tag, children=text_to_children(content), props=None)
        
        elif block_type == "paragraph":
            html_node = ParentNode(tag="p", children=text_to_children(block), props=None)
        
        elif block_type == "quote":
            content = block.lstrip("> ").strip()
            html_node = ParentNode(tag="blockquote", children=text_to_children(content), props=None)
        
        elif block_type == "unordered_list":
            items = block.splitlines()
            list_children = [ParentNode(tag="li", children=text_to_children(item.strip().lstrip("-*").strip())) for item in items]
            html_node = ParentNode(tag="ul", children=list_children, props=None)
        
        else:
            continue # skip unknown block types
        
        if html_node:
            children.append(html_node)
    
    return ParentNode(tag="div", children=children, props=None)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = [text_node_to_html(node) for node in text_nodes]
    return children