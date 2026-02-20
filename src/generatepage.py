from block_split import markdown_to_html_node
import os

'''
    Extracts title, an <h1> header from the markdown file, and returns it 
    Args:
        markdown (str): REQUIRED - Raw Markdown text to extract title from
    Returns:
        str: Title extracted from MD file with # and any leading or trailing whitespace removed
            or an Exception 
'''
def extract_title(markdown: str):
    lines = markdown.split("\n") 

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()

    raise ValueError("No title found in markdown, ensure there is a single h1 header")

def generate_page(from_path, template_path, dest_path): 
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")

    markdown, template = None, None

    # Read markdown file from from_path
    with open(from_path, "r") as f:
        markdown = f.read() 

    # Read template file from template_path
    with open(template_path, "r") as f:
        template = f.read()
    
    html_string = markdown_to_html_node(markdown).to_html()

    title = extract_title(markdown) 

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)

    # Write the new HTML page to dest_path 
    if not os.path.dirname(dest_path): 
        os.makedirs(os.path.dirname(dest_path))
    
    with open(dest_path, "w") as f:
        f.write(template)



    
