import speech_recognition as sr

class listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.pause_threshold = 0.8
        self.recognizer.non_speaking_duration = 0.3
    
    def listen(self):
        with sr.Microphone() as src:
            
            self.recognizer.adjust_for_ambient_noise(src, duration=0.5)

            audio = self.recognizer.listen(src, timeout = 5, phrase_time_limit = 8)

            try:
                text = self.recognizer.recognize_google(audio)
                return True, text.lower()
            except sr.UnknownValueError:
                return False, "sorry, couldn't understand what you said.please try again."
            
            except sr.RequestError:
                return False, "sorry, unable to connect to google services."