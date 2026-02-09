from enum import Enum
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
        list[]
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
