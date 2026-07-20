from webbrowser import open as webopen
from json import load
from utils.paths import DATA

KEYWORDS = (
    "go to website",
    "visit website",
)

def website_opener(txt):
    txt = txt.lower()
    if not any(keyword in txt for keyword in KEYWORDS):
        return False,""
    
    with open(DATA / "websites.json") as file:
        websites = load(file)
        
        for website in websites:
            if website in txt:
                webopen(websites[website])
                return True, f"sure! opening {website}"
            
        return True, "sorry, i don't know that website yet. would you like me to learn it?"
    
            
