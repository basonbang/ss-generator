from enum import Enum 

'''
    Enum for the different types of inline text nodes
'''
class TextType(Enum): 
    PLAIN_TEXT = 1
    BOLD_TEXT = 2
    ITALIC_TEXT = 3
    CODE = 4
    LINK = 5
    IMAGE = 6

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = ""):
        self.text = text
        self.text_type = text_type
        self.url = url  # Used for links and images, defaulted to none
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False 
        
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
