from json import load, dump
from tkinter import Tk , filedialog
from utils.paths import DATA

KEYWORDS = (
    "learn app",
    "remember app",
    "add app",
)

def learn_app_confirmer(txt):
    if any(keyword in txt for keyword in KEYWORDS):
        return "What should i call it?"
    return None
    
def learn_app(name):
    name = name.lower()

    selector = Tk()
    selector.withdraw()

    path = filedialog.askopenfilename(
        title="Select an Executable",
        filetypes=[("Executable files", "*.exe")]
        )
    selector.destroy()

    if not path:
        return "no apps were selected."

    with open(DATA / "apps.json", "r") as file:
        apps = load(file)

    if name in apps:
        return f"{name} is already learned. Would you like me to open it now?"

    apps[name] = path

    with open(DATA / "apps.json", "w") as file:
        dump(apps, file, indent=4)

    return f"{name} has been learned. Would you like me to open it now?"