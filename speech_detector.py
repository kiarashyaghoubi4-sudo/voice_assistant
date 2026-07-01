import speech_recognition as sr


class listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    
    def listen(self):
        with sr.Microphone() as src:
            print("listening...")
            
            self.recognizer.adjust_for_ambient_noise(src, duration=1)

            audio = self.recognizer.listen(src)
            try:
                text = self.recognizer.recognize_google(audio)
                return text.lower()
            except sr.UnknownValueError:
                return None
            except sr.RequestError:
                return None



