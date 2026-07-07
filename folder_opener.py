from default_folders import DEFAULT_FOLDERS
from json import load
from os import startfile

def open_folder(txt):
    txt = txt.lower()

    with open("folders.json","r") as user_folders_json:
        user_folders = load(user_folders_json)

        folders = DEFAULT_FOLDERS.copy()
        folders.update(user_folders)

    for folder, path in folders.items():
        if folder in txt:
            startfile(path)
            return f"sure! opening {folder}"

    return "sorry.i don't know that folder yet.would you like me to learn it?"
