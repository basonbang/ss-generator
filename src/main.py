from textnode import *
from os import path
from shutil import rmtree
from copystatic import copy_directory
from generatepage import generate_page

def main():
    static_path = path.join(path.dirname(path.dirname(__file__)), "static")
    public_path = path.join(path.dirname(path.dirname(__file__)), "public")

    if path.exists(public_path):
        print(f"Public directory {public_path} already exists, deleting it to keep copy clean.")
        rmtree(public_path)

    copy_directory(static_path, public_path)

    src_dir = path.dirname(__file__)
    from_path = path.join(src_dir, "content/index.md")
    template_path = path.join(src_dir, "template.html")
    to_path = path.join(public_path, "index.html")

    generate_page(from_path, template_path, to_path)

if __name__ == "__main__":
    main()