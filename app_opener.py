from os import startfile
from json import load

def open_app(txt):
    txt = txt.lower()
    with open("apps.json","r") as file:
        apps = load(file)
        for app in apps:
            if app in txt:
                startfile(apps[app])

                return f"sure! opening {app}."
                
    return f"sorry.but i don't know that app yet.would you like me to learn it?"