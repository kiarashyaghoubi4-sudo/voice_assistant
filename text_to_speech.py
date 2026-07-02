import pyttsx3

class speaker:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self,txt):
        self.engine.say(txt)
        self.engine.runAndWait()
