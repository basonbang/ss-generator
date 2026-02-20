from os import path, listdir, mkdir
from shutil import copy, rmtree

'''
    Utility function to copy directory from source to destination
    Args:
        src (str): REQUIRED - Source directory path
        dst (str): REQUIRED - Destination directory path
    Returns:
        None

'''
def copy_directory(src: str, dest: str):
    if not path.exists(src):
        raise ValueError("Source directory does not exist")
    
    if path.exists(dest):
        raise ValueError("Destination directory already exists, should've been removed")
    
    # Create destination directory
    mkdir(dest)
    # print(f"Created destination directory {dest}")

    for direntry in listdir(src):
        src_entry = path.join(src, direntry)
        dest_entry = path.join(dest, direntry)

        # print(f"Copying {src_entry} to {dest_entry}")

        if path.isfile(src_entry):
            # print(f"{src_entry} is a file, copying...\n")
            copy(src_entry, dest_entry)
        else:
            # print(f"{src_entry} is a directory, copying recursively...\n")
            copy_directory(src_entry, dest_entry)
    
