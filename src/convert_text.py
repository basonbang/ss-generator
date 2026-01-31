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

        split_text = old_node.text.split() 
        text_around_delimiter = []
        plain_text = []
        scanning_for_close_delimiter = False

        for word in split_text:
            if delimiter in word:
                # If the delimiter appears twice in the same word
                if word.count(delimiter) == 2:
                    text_without_delimiter = word.split(delimiter)
                    node = TextNode(text_without_delimiter[1],text_type)
                    new_nodes.append(node)
                    continue
                
                # If we come across the opening delimiter
                if scanning_for_close_delimiter == False:
                    scanning_for_close_delimiter = True
                    text_around_delimiter.append(word.split(delimiter)[1])

                    # Create TextNode for any plain text before delimiter
                    if plain_text:
                        plain_text_str = " ".join(plain_text)
                        plain_text_node = TextNode(plain_text_str, TextType.PLAIN_TEXT)
                        new_nodes.append(plain_text_node)
                        plain_text = []
                    continue

                # If we come across the closing delimiter
                elif scanning_for_close_delimiter == True:
                    text_around_delimiter.append(word.split(delimiter)[0])
                    delimiter_text = " ".join(text_around_delimiter)
                    node = TextNode(delimiter_text, text_type)
                    new_nodes.append(node)
                    scanning_for_close_delimiter = False
                    text_around_delimiter = []
                    continue
                    
            # Non-delimiter text, either part of plain text or in between delimiters
            if scanning_for_close_delimiter == True:
                text_around_delimiter.append(word)
                continue 
            else:
                plain_text.append(word)

        # Closing delimiter was not found in the text
        if text_around_delimiter:
            raise Exception(f"Unmatched delimiter '{delimiter}' found in text: '{split_text}'")
        
        # Create TextNode for any remaining plain text after processing
        if plain_text:
            plain_text_str = " ".join(plain_text)
            plain_text_node = TextNode(plain_text_str, TextType.PLAIN_TEXT)
            new_nodes.append(plain_text_node)
            plain_text = []

    return new_nodes
        



        
        
        