#!/usr/bin/env python3

"""
Create folders from a list in current directory
"""
from pathlib import Path

with open("folder_list.txt", "r") as f:
    for folder_path in f.readlines():
         # Remove new line character
        folder_path = folder_path.strip()
        path = Path.cwd() / folder_path
        try:
            path.mkdir(exist_ok=False)
        except FileExistsError:
            print (f"{path} already exists")
        except OSError:
            print (f"Could not create the folder {path}")

