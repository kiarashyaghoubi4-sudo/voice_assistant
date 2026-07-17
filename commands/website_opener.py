from webbrowser import open as webopen
from json import load

KEYWORDS = (
    "go to website",
    "visit website",
)

def website_opener(txt):
    txt = txt.lower()
    if not any(keyword in txt for keyword in KEYWORDS):
        return None
    with open("data/websites.json") as file:
        websites = load(file)
        
        for website in websites:
            if website in txt:
                webopen(websites[website])
                return f"sure! opening {website}"
            
        return "sorry, i don't know that website yet. would you like me to learn it?"
    
            
