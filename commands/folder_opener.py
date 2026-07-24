from data.default_folders import DEFAULT_FOLDERS
from json import load
from os import startfile
from utils.paths import DATA

KEYWORDS = (
    "open folder",
    "launch folder",
    "run folder",
)

def open_folder(txt):
    txt = txt.lower()

    if not any(keyword in txt for keyword in KEYWORDS):
        return False, ""

    with open(DATA / "folders.json","r") as user_folders_json:
        user_folders = load(user_folders_json)

        folders = DEFAULT_FOLDERS.copy()
        folders.update(user_folders)

    for folder, path in folders.items():
        if folder in txt:
            startfile(path)
            return True, f"sure! opening {folder}"

    return True, "sorry, but i don't know that folder yet.would you like me to learn it?"
