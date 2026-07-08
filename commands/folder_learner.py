from json import load, dump
from tkinter import Tk , filedialog

def learn_folder_confirmer(txt):
    if ("learn" in txt) and ("folder" in txt):
        return "What should i call it?"
    
def learn_folder(name):
    name = name.lower()
    selector = Tk()
    selector.withdraw()

    path = filedialog.askdirectory(
        title="Select a folder",
        )
    selector.destroy()

    if not path:
        return "no folders were selected"

    with open("data/folders.json", "r") as file:
        folders = load(file)

    if name in folders:
        return f'folder "{name}" is already learned. Would you like me to open it now?'

    folders[name] = path

    with open("data/folders.json", "w") as file:
        dump(folders, file, indent=4)

    return f'folder "{name}" has been learned. Would you like me to open it now?'