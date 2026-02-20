class HTMLNode:

    '''
    HTMLNode class
    Args:
        tag (str | None): The HTML tag of the node
        value (str | None): The value of the HTML tag
        children (list[HTMLNode] | None): List of child HTMLNode objects. Defaults to None.
        props (dict[str, str] | None): Dictionary of HTML properties/attributes. Defaults to None.
    '''
    def __init__(self, tag: str | None = None, value: str | None = None, children: list["HTMLNode"] | None = None, props: dict[str, str] | None = None):
        self.tag = tag 
        self.value = value 
        self.children = children 
        self.props = props
    
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

class LeafNode(HTMLNode):
    '''
        LeafNode is a subclass of HTMLNode, representing HTML nodes with no children.
        Args:
            tag (str | None): REQUIRED, but may be None - The HTML tag of the node
            value (str): REQUIRED - The value of the HTML tag 
            props (dict[str, str] | None): OPTIONAL - Dictionary of HTML properties/attributes. Defaults to None.
    '''
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All LeafNode objects must have a value")
        
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

class ParentNode(HTMLNode):
    '''
        ParentNode is a subclass of HTMLNode, any HTMLNode that has children/isn't a leaf node is a parent node.
        Args:
            tag (str): REQUIRED - The HTML tag of the node
            children (list[HTMLNode]): REQUIRED - List of child HTMLNode objects
            props (dict[str, str] | None): OPTIONAL - Dictionary of HTML properties/attributes. Defaults to None.
    '''
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode objects must have a tag")
        
        if self.children is None:
            raise ValueError("ParentNode objects must have children")
        
        html_string = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            html_string += child.to_html()
        
        html_string += f"</{self.tag}>" 
        return html_string
    
    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"