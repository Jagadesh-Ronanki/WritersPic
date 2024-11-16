# bot/utils.py

import os
import shutil

def parse_input(input_text):
    """
    Parse the input text from the user to separate heading and content.
    """
    lines = input_text.splitlines()
    heading = ""
    content = []
    current_paragraph = ""

    for line in lines:
        line = line.strip()
        if line.startswith("!generate"):
            continue
        elif line.startswith("[Heading]"):
            heading = line.replace("[Heading]", "").strip()
        elif line.startswith("[Content]"):
            continue
        elif line.startswith("bt[") or line.startswith("st[") or line.startswith("Items["):
            if current_paragraph:
                content.append(current_paragraph.strip())
                current_paragraph = ""
            content.append(line)
        elif line == "":
            if current_paragraph:
                content.append(current_paragraph.strip())
                current_paragraph = ""
        else:
            if current_paragraph:
                current_paragraph += " " + line
            else:
                current_paragraph = line

    if current_paragraph:
        content.append(current_paragraph.strip())

    return content[0], content[1:]


def cleanup_generated_files(folder_path):
    """Deletes the folder and its contents."""
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Deleted folder: {folder_path}")
    else:
        print(f"Folder not found: {folder_path}")
