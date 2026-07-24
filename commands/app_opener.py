from os import startfile
from json import load
from utils.paths import DATA
KEYWORDS = (
    "open",
    "launch",
    "run",
)
def open_app(txt):
    txt = txt.lower()
    
    if not any(keyword in txt for keyword in KEYWORDS):
        return False, ""
    
    with open(DATA / "apps.json","r") as file:
        apps = load(file)
        for app in apps:
            if app in txt:
                startfile(apps[app])

                return True, f"sure! opening {app}."
                
    return True, "sorry, but i don't know that app yet.would you like me to learn it?"