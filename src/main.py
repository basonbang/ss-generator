from textnode import *
from os import path
from shutil import rmtree
from copystatic import copy_directory
from generatepage import generate_pages_recursive

def main():
    src_dir = path.dirname(__file__)
    root_dir = path.dirname(src_dir)
    static_path = path.join(root_dir, "static")
    public_path = path.join(root_dir, "public")

    if path.exists(public_path):
        print(f"Public directory {public_path} already exists, deleting it to keep copy clean.")
        rmtree(public_path)

    copy_directory(static_path, public_path)


    content_path = path.join(root_dir, "content")
    template_path = path.join(src_dir, "template.html")

    generate_pages_recursive(content_path, template_path, public_path)

if __name__ == "__main__":
    main()