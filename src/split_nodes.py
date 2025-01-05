from textnode import TextNode, TextType
from extract_links import *

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        # Non-text nodes are appended as-is.
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        # list of images are created
        image_list = extract_markdown_images(node.text)
        # if there are no images, append the original nodes
        if not image_list:
            new_nodes.append(node)
            continue

        # process text and split based on images
        remaining_text = node.text
        for alt_text, image_url in image_list:
            # splits node.text into sections around the image
            pre_text, _, remaining_text = remaining_text.partition(f"![{alt_text}]({image_url})")
            # adds text before image
            if pre_text:
                new_nodes.append(TextNode(pre_text, TextType.TEXT))
            # adds the image text
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
        # adds text after the image
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    
   # retruns list but removes empty nodes
    return [node for node in new_nodes if node.text]


def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        # Non-text nodes are appended as-is.
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        # list of links are created
        links_list = extract_markdown_links(node.text)
        # if there are no links, append the original nodes
        if not links_list:
            new_nodes.append(node)
            continue

        # process text and split based on links
        remaining_text = node.text
        for link_text, link_url in links_list:
            # splits node.text into sections around the link
            pre_text, _, remaining_text = remaining_text.partition(f"![{link_text}]({link_url})")
            # adds text before link
            if pre_text:
                new_nodes.append(TextNode(pre_text, TextType.TEXT))
            # adds the link text
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
        # adds text after the link
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    
   # retruns list but removes empty nodes
    return [node for node in new_nodes if node.text]