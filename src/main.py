from textnode import *
from os import path
from shutil import rmtree
from copystatic import copy_directory
from generatepage import generate_pages_recursive
import sys 

def main():
    # default basepath is "/" since site assumes it's being served from the root
    # but will be set to first command line arg if provided.
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'

    src_dir = path.dirname(__file__)
    root_dir = path.dirname(src_dir)
    static_path = path.join(root_dir, "static")
    docs_path = path.join(root_dir, "docs")

    if path.exists(docs_path):
        print(f"Docs directory {docs_path} already exists, deleting it to keep copy clean.")
        rmtree(docs_path)
    copy_directory(static_path, docs_path)


    content_path = path.join(root_dir, "content")
    template_path = path.join(src_dir, "template.html")

    generate_pages_recursive(content_path, template_path, docs_path, basepath)

if __name__ == "__main__":
    main()