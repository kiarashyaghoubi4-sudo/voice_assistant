from json import load, dump
import customtkinter as ctk

KEYWORDS = (
    "learn website",
    "remember website",
    "add website",
)

def learn_website_confirmer(txt):
    if any(keyword in txt for keyword in KEYWORDS):
        return "sure!What should i call it?"
    return None
    
def get_url():

    window = ctk.CTk()

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")


    window.title("Learn Website")
    window.geometry("400x170")


    
        
    label = ctk.CTkLabel(
        window,
        text="Please enter the website URL:"
    )

    label.pack(pady = (20, 10))

    entry = ctk.CTkEntry(
    window,
    width=300,
    placeholder_text="https://example.com"
    )

    entry.pack()

    url = None

    def save():
        nonlocal url
        url = entry.get()
        window.destroy()

    button = ctk.CTkButton(
    window,
    text="Save"
)
    button.configure(command=save)
    button.pack(pady=20)

    entry.focus()

    entry.bind("<Return>", lambda event: save())

    window.mainloop()


    return url

def learn_website(name, url):
    if not url:
        return "App learning canceled."
    
    url = url.lower()

    with open("data/websites.json","r") as file:
        websites = load(file)

    if name in websites:
        return f'website "{name}" is already learned. Would you like me to open it now?'
    
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    websites[name] = url

    with open("data/apps.json", "w") as file:
        dump(websites, file, indent=4)

    return f'website "{name}" has been learned. Would you like me to open it now?'