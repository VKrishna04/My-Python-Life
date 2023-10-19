# Getting all the paths to make jupyter notebook for 100 days of code from all the notes.

import os

def get_md_file_paths(directory):
    md_file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                md_file_paths.append(os.path.join(root, file))

    md_file_paths.sort()  # Sort the paths alphabetically
    return md_file_paths

# Example usage:
directory = r"F:\Code\Coding\Python\100-days-of-code-youtube"
md_paths = get_md_file_paths(directory)
print(md_paths)
