class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # Will be overridden by child classes that render themselves as HTML
    def to_html(self):
        raise NotImplementedError
    
    # Converts props dictionary to a string
    def props_to_html(self):
        # handles None or empty props
        if not self.props:
            return ""
        # convert props dictionary to a string with = and no commas.
        props_as_string = " ".join(f"{key}='{value}'" for key, value in self.props.items())
        return props_as_string
    
    # Prints HTMLNode instance for debugging purposes.
    def __repr__(self):
        children_repr = ", ".join(self.children)
        props_repr = " ".join(f"{key}:{value}" for key, value in self.props.items())
        return (f"HTMLNode(tag={self.tag}, value={self.value}, children=[{children_repr}], props={{ {props_repr}}})")