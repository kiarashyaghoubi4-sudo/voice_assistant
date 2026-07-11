from json import load, dump
from tkinter import Tk , filedialog

def learn_app_confirmer(txt):
    if ("learn" in txt) and ("app" in txt):
        return "What should i call it?"
    
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

    with open("data/apps.json", "r") as file:
        apps = load(file)

    if name in apps:
        return f"{name} is already learned. Would you like me to open it now?"

    apps[name] = path

    with open("data/apps.json", "w") as file:
        dump(apps, file, indent=4)

    return f"{name} has been learned. Would you like me to open it now?"