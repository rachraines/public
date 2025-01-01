from leafnode import LeafNode
from textnode import TextNode, TextType

# converts textnode to HTMLnode
def text_node_to_html(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise ValueError("Invalid TextType")
    elif text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        if text_node.url == None:
            raise ValueError("TextNode must have a URL")
        else:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        if text_node.url == None:
            raise ValueError("TextNode must have a URL")
        else:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text or "alt text"})
    else:
        raise NotImplementedError(f"HTML conversion for {text_node.text_type} is not implented.")