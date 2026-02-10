from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import *
from inline_split import text_to_textnodes

import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

'''
    Takes a raw Markdown string (representing full doc) and returns a list of block strings
    Args:
        markdown (str): REQUIRED 
    Returns:
        list[str]: List of block strings, each block represents separate block of Markdown text
'''
def markdown_to_blocks(markdown: str):
    blocks = []
    split_by_newlines = markdown.split("\n\n")

    for block in split_by_newlines:
        if block.strip() != "":
            blocks.append(block.strip())

    return blocks

'''
    Takes a single block of Markdown text and returns the corresponding BlockType
    All leading and trailing whitespace has already been stripped.
    Args:
        markdown (str): REQUIRED 
    Returns:
        blocktype (BlockType)
'''
def block_to_blocktype(markdown: str):   

    lines = markdown.split("\n")

    if (re.match(r"#{1,6} .+", markdown)):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if (markdown.startswith(">")):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if (markdown.startswith("- ")):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if markdown.startswith("1. "):
        for i, line in enumerate(lines):
            if not line.startswith(f"{i+1}. "):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

'''
    Converts a full Markdown doc into a single parent HTMLNode with children representing each
    block of Markdown text.
    Args:
        markdown (str): REQUIRED - Full Markdown document to convert into HTMLNode tree
    Returns:
        HTMLNode: Root node of the resulting HTMLNode tree representing the full Markdown document
'''
def markdown_to_html_node(markdown: str):
    # Get all separate blocks of Markdown from full doc
    blocks = markdown_to_blocks(markdown)

    # Create parent node with tag "div"
    parent = ParentNode(tag="div", children=[])
    parent_children = []

    for block in blocks:
        # Determine block type
        block_type = block_to_blocktype(block)

        # Convert block to corresponding HTMLNode based on block type
        match block_type:
            case BlockType.PARAGRAPH:
                block_text = block.replace("\n", " ")
                paragraph_node = ParentNode(tag="p", children=text_to_children(block_text))
                parent_children.append(paragraph_node)
            case BlockType.HEADING:
                heading_node = heading_to_htmlnode(block)
                parent_children.append(heading_node)
            case BlockType.CODE:
                code_block = code_block_to_htmlnode(block)
                parent_children.append(code_block)
            case BlockType.QUOTE:
                quote_node = LeafNode(tag="blockquote", value=block[1:].strip())
                parent_children.append(quote_node)
            case BlockType.UNORDERED_LIST:
                ul_node = unordered_list_to_htmlnode(block)
                parent_children.append(ul_node)
            case BlockType.ORDERED_LIST:
                ol_node = ordered_list_to_htmlnode(block)
                parent_children.append(ol_node)
    
    parent.children = parent_children
    return parent

'''
    Converts a block representing an unordered list into corresponding HTMLNode with 
    it's children representing each list item
    Args:
        block (str): REQUIRED 
    Returns:
        HTMLNode: Root node of the resulting HTMLNode 
'''
def unordered_list_to_htmlnode(block: str):
    # Create parent node with tag "ul"
    parent = ParentNode(tag="ul", children=[])

    # Get list items from the unordered list block
    items = block.split("\n")

    parent_children = []

    for item in items:
        # Remove "-" marker from beginning of list item
        if item.startswith("- "):
            item = item[2:]
        else:
            raise ValueError("Invalid unordered list item, must start with '- '")
        
        # Create list item HTML node
        list_item_node = ParentNode(tag="li", children=text_to_children(item))

        # Add list item node to parent node's children
        parent_children.append(list_item_node)
    
    parent.children = parent_children
    return parent

'''
    Converts a block representing an ordered list into corresponding HTMLNode with 
    it's children representing each list item
    Args:
        block (str): REQUIRED 
    Returns:
        HTMLNode: Root node of the resulting HTMLNode
'''
def ordered_list_to_htmlnode(block: str):
    parent = ParentNode(tag="ol", children=[])
    items = block.split("\n")
    parent_children = []

    for item in items:
        # Remove numeric prefix from beginning of list item
        if re.match(r"\d+\. ", item):
            item = re.sub(r"^\d+\. ", "", item)
        else:
            raise ValueError("Invalid ordered list item, must start with numeric prefix like '1. '")
        
        list_item_node = ParentNode(tag="li", children=text_to_children(item))
        parent_children.append(list_item_node)
    
    parent.children = parent_children
    return parent

'''
    Converts a block representing a code block into corresponding HTMLNode with it's value
    representing the code text. The code block is also nested within a <pre> tag
    Args:
        block (str): REQUIRED
    Returns:
        HTMLNode: Root node of the resulting HTMLNode
'''
def code_block_to_htmlnode(block: str):
    # Create parent node with tag "pre"
    parent = ParentNode(tag="pre", children=[])
    # Remove backtick markers and leading/trailing newlines from the block text
    lines = block.split("\n")
    code_text = "\n".join(lines[1:-1])
    # Create child node with tag "code" and value representing the code text
    code_node = TextNode(code_text, TextType.CODE).text_node_to_html_node()
    parent.children = [code_node]

    return parent

'''
    Converts a block representing a heading into corresponding HTMLNode with it's value
    representing the heading text. The heading level is determined by the number of leading "#" characters
    Args:
        block (str): REQUIRED
    Returns:
        HTMLNode: Root node of the resulting HTMLNode
'''
def heading_to_htmlnode(block: str):
    # Count number of leading # characters 
    match = re.match(r"^(#{1,6}) ", block)
    
    if not match:
        raise ValueError("Invalid heading block, must start with 1-6 '#' characters followed by a space")
    
    # Get capture group - string of # chars - and use length to determine heading level
    heading_level = len(match.group(1))
    # Remove leading # chars + the space and strip leading/trailing whitespace
    block_text = block[heading_level+1:].strip()

    parent = ParentNode(tag=f"h{heading_level}", children=text_to_children(block_text))

    return parent

'''
    Takes a string of text and converts it to a list of HTMLObjects representing the 
    inline formatting in the text
    Args:
        text (str): REQUIRED - The text to convert into a list of HTMLObjects
    Returns:
        list[HTMLNode]
'''
def text_to_children(text: str):
    # Get a list of the various inline formatting within the text
    inline_text_nodes = text_to_textnodes(text)

    html_nodes = []

    # Convert each TextNode to HTMLNodes 
    for node in inline_text_nodes:
        html_node = node.text_node_to_html_node()
        html_nodes.append(html_node)

    return html_nodes