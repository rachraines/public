from enum import Enum
from leafnode import LeafNode

# acceptable text types
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE =  "code"
    LINK = "link"
    IMAGE = "image"

# creates text node instances
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # checks if two text nodes have the exact same properties
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    # creates a string representation of the TextNode
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
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
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        elif text_node.text_type == TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text or "alt text"})
        else:
            raise NotImplementedError(f"HTML conversion for {text_node.text_type} is not implented.")