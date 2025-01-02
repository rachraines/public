from text_to_html import TextNode, TextType

from enum import Enum

# acceptable delimiter types
class Delimiter(Enum):
    BOLD = "**"
    ITALIC = "*"
    CODE =  "`"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []

    # raises error if incorrect delimiter given
    if delimiter not in [d.value for d in Delimiter]:
        raise ValueError("Delimiter not valid")
    
    for node in old_nodes:
        # if not a text node, add it as-is
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
            
        parts_of_text = node.text.split(delimiter)
        # if the length of the list is even, there is an unmatched delimiter
        if len(parts_of_text) % 2 == 0:
            raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")
        # rebuild nodes based on split
        for i, part in enumerate(parts_of_text): # indexes the part in the list
            if part: # ignores empty strings from the split
                if i % 2 == 0:
                    # outside of the delimiters: plain text
                    new_list.append(TextNode(part, TextType.TEXT))
                else:
                    # inside the delimiters
                    new_list.append(TextNode(part, text_type))
            
    return new_list
    
