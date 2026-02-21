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

'''
    Generates a static HTML page from a MD file and an HTML template, writing result to destination path
    Args:
        from_path (str): REQUIRED - Path to source MD file to convert into HTML page
        template_path (str): REQUIRED - Path to HTML template file
        dest_path (str): REQUIRED - Path to destination HTML file
        basepath (str): OPTIONAL - Base path to use for generated links in HTML page, default is "/"
    Returns:
        None - Should write page to dest_path
'''
def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str = "/"): 
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

    # Replace links that start from root with the basepath+link
    template = template.replace(f'href="/', f'href="{basepath}')
    template = template.replace(f'src="/', f'src="{basepath}')

    # Write the new HTML page to dest_path 
    dest_dir_path = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    
    with open(dest_path, "w") as f:
        f.write(template)

'''
    Generates static HTML pages for all MD files in a directory, writing results to destination directory
    Args:
        dir_path_content (str): REQUIRED - Path to source directory containing MD files to convert into HTML pages
        template_path (str): REQUIRED - Path to HTML template file
        dest_dir (str): REQUIRED - Path to destination directory to write generated HTML pages to
        basepath (str): OPTIONAL - Base path to use for generated links in HTML pages, default is "/"
    Returns:
        None - Should write pages to dest_dir

'''
def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir: str, basepath: str = "/"):

    # Crawl every entry within content directory 
    for direntry in os.listdir(dir_path_content):

        # Construct full path for content entry and destination entry
        content_entry = os.path.join(dir_path_content, direntry)
        dest_entry = os.path.join(dest_dir, direntry)

        # If entry is a markdown file, generate it's HTML page
        if os.path.isfile(content_entry) and content_entry.endswith(".md"):
            dest_entry = dest_entry[:-3] + ".html"
            generate_page(content_entry, template_path, dest_entry, basepath)
        else:
            generate_pages_recursive(content_entry, template_path, dest_entry, basepath)

