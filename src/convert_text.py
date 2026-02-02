from textnode import TextNode, TextType 

'''
    Creates TextNode objects from raw Markdown strings by splitting on a given delimiter.

    Args:
        old_nodes (list[TextNode])
            REQUIRED - List of TextNode objects to split (Raw Markdown)
        delimiter (str)
            REQUIRED - Delimiter string to split TextNode objects by
        text_type (TextType)
            REQUIRED - The TextType to assign to certain split segments
    Returns:
        new_nodes (list[TextNode])
            List of TextNode objects created after splitting old nodes by the delimiter
    Example:
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        # new_nodes will contain:
            [
                TextNode("This is text with a ", TextType.TEXT),  
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT)
            ]
'''
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    #TODO: Support nested inline elements (e.g., bold text inside code blocks)
    new_nodes = []

    for old_node in old_nodes:
        # We only want to split plain text nodes, as it comes from raw markdown
        # Add non-plain text nodes directly to new_nodes
        if old_node.text_type != TextType.PLAIN_TEXT: 
            new_nodes.append(old_node)
            continue 

        split_text = old_node.text.split(delimiter)
        split_nodes = []
        
        # Invalid Markdown if even number of elements in the split text
        # No elements = no delimiters found, 2, 4, 6.. = unmatched delimiters
        if len(split_text) % 2 == 0:
            raise Exception(f"Unmatched delimiter '{delimiter}' found in text: '{old_node.text}'")
     
        for i, segment in enumerate(split_text):
            # Some segments may be empty strings due to consecutive delimiters (e.g., "**bold**")
            if segment == "":
                continue

            if i % 2 == 0:
                # Plain text
                split_nodes.append(TextNode(segment, TextType.PLAIN_TEXT))
            else:
                # Delimited text
                split_nodes.append(TextNode(segment, text_type))

        new_nodes.extend(split_nodes)

    return new_nodes
        



        
        
        