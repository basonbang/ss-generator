class HTMLNode:

    '''
    HTMLNode constructor
    Args:
        tag (str | None): The HTML tag of the node
        value (str | None): The value of the HTML tag (e.g. text inside a paragraph)
        children (list[HTMLNode] | None): List of child HTMLNode objects. Defaults to None.
        props (dict[str, str] | None): Dictionary of HTML properties/attributes. Defaults to None.
    '''
    def __init__(self, tag: str | None = None, value: str | None = None, children: list["HTMLNode"] | None = None, props: dict[str, str] | None = None):
        self.tag = tag if tag is not None else ""
        self.value = value if value is not None else ""
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented yet")

    '''
    Returns a formatted string representing the HTML node's attributes
    '''
    def props_to_html(self): 
        if self.props is None:
            return ""
        
        attr_string = ""

        for prop in self.props:
            attr_string += f' {prop}="{self.props[prop]}"'
    
        return attr_string
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

'''
    LeafNode is a subclass of HTMLNode, representing HTML nodes with no children.
'''
class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] | None = None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All LeafNode objects must have a value")
        
        if not self.tag:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"