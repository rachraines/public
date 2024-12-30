from htmlnode import HTMLNode

# Creates LeafNode as a child class inheriting from HTMLNode
class LeafNode(HTMLNode):
    # Inherits tags, value, and props (no children)
    def __init__(self, tag=None, value=None, props=None):
        
        # Value cannot be none
        if value is None:
            raise ValueError("A LeafNode must have a value")
        
        # Inherits all inputs from the super class but sets children automatically to None.
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        # Value cannot be none
        if self.value is None:
            raise ValueError("A LeafNode must have a value")
        elif self.tag is None:
            return self.value
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"