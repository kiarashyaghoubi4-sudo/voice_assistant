from webbrowser import open as webopen
from json import load

def website_opener(txt):
    with open("/datawebsites.json") as file:
        websites = load(file)
        
        for website in websites:
            if website in txt:
                webopen(websites[website])
                return f"sure! opening {website}"
            
            return "sorry, i don't know that website yet. would you like me to learn it?"
    
            
