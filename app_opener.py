from os import startfile
from json import load, dump
from tkinter import Tk , filedialog

def open_app(txt):
    txt = txt.lower()
    with open("apps.json") as file:
        apps = load(file)
        for app in apps:
            if app in txt and "open" in txt or app in txt and "launch" in txt or app in txt:
                startfile(apps[app])
