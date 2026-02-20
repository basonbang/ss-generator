from textnode import *
from os import path
from shutil import rmtree
from copystatic import copy_directory

def main():
    static_path = path.join(path.dirname(path.dirname(__file__)), "static")
    public_path = path.join(path.dirname(path.dirname(__file__)), "public")

    if path.exists(public_path):
        print(f"Public directory {public_path} already exists, deleting it to keep copy clean.")
        rmtree(public_path)

    copy_directory(static_path, public_path)
    
if __name__ == "__main__":
    main()