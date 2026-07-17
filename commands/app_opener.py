from os import startfile
from json import load

KEYWORDS = (
    "open app",
    "launch app",
    "run app",
)
def open_app(txt):
    txt = txt.lower()
    
    if not any(keyword in txt for keyword in KEYWORDS):
        return None
    
    with open("data/apps.json","r") as file:
        apps = load(file)
        for app in apps:
            if app in txt:
                startfile(apps[app])

                return f"sure! opening {app}."
                
    return f"sorry.but i don't know that app yet.would you like me to learn it?"