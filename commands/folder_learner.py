from json import load, dump
from tkinter import Tk , filedialog
from utils.paths import DATA
KEYWORDS = (
    "learn folder",
    "remember foler",
    "add folder",
)

def learn_folder_confirmer(txt):
    if any(keyword in txt for keyword in KEYWORDS):
        return "What should i call it?"
    return None
    
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

    with open(DATA / "folders.json", "r") as file:
        folders = load(file)

    if name in folders:
        return f'folder "{name}" is already learned. Would you like me to open it now?'

    folders[name] = path

    with open(DATA / "folders.json", "w") as file:
        dump(folders, file, indent=4)

    return f'folder "{name}" has been learned. Would you like me to open it now?'