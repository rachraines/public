from htmlnode import HTMLNode

# Creates ParentNode as a child class inheriting from HTMLNode
class ParentNode(HTMLNode):
    # Inherits tags, children, and props (no value)
    def __init__(self, tag=None, children=None, props=None):
        
        # Children and tag cannot be none
        if children is None:
            raise ValueError("A ParentNode must have children")
        if tag is None:
            raise ValueError("A ParentNode must have a tag")
        
        # Inherits all inputs from the super class but sets value automatically to None.
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        # Tag cannot be none
        if self.tag is None:
            raise ValueError("A ParentNode must have a tag")
        # Children cannot be none
        if self.children is None:
            raise ValueError("A ParentNode must have children")
        
        # Generate HTML for each child recursively
        children_html = "".join(child.to_html() for child in self.children)
        
        # Generates props HTML if present
        props_html = f" {self.props_to_html()}" if self.props else ""

        # Returns full HTML
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"
        