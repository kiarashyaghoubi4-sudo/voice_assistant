from commands.app_learner import learn_app_confirmer, learn_app
from commands.app_opener import  open_app
from commands.folder_learner import learn_folder_confirmer, learn_folder
from commands.folder_opener import open_folder
from commands.website_learner import learn_website_confirmer, learn_website, get_url
from commands.website_opener import website_opener
from commands.system_commands import shutdown_confirmation, shutdown,restart_confirmation, restart, lock, log_out_confirmation, log_out, sleep, hibernate 
from gui import dashboard
from speech import speech_to_text, text_to_speech, wake_word


class Assistant:

    def __init__(self):
        self.listener = speech_to_text.listener()
        self.speaker = text_to_speech.speaker()
        self.window = dashboard.Dashboard()
    
    def setup(self):
        self.window.set_status(dashboard.Dashboard.IDLE)
        self.window.show_msg("hello! how can i help you today?", dashboard.Dashboard.BOT)
        self.window.start_window()
        self.speaker.speak("hello! how can i help you today?")

    def wake(self):
        wake_word.wait_for_wake_word()
        self.setup()

        
    def listen(self):
        self.window.set_status(dashboard.Dashboard.LISTENING)
        command = self.listener.listen().lower()
        self.window.show_msg(command, dashboard.Dashboard.USER)
        return command
    
    def say(self, msg, sender):
        self.window.show_msg(msg, sender)
        self.speaker.speak(msg)

    def sleep(self):
        self.window.destroy_window()

    
    def handle_opening(self, command):

        handled, message = open_app(command)

        if handled:
            self.say(message)
            return True

        handled, message = open_folder(command)

        if handled:
            self.say(message)
            return True

        handled, message = website_opener(command)

        if handled:
            self.say(message)
            return True

        return False
    
    def handle_learning(self, command):
        handled, message = learn_website_confirmer(command)

        if handled:
            self.say(message)
            name = self.listener.listen()
            url = get_url()
            learn_website(name, url)
            return True

        handled, message = learn_folder_confirmer(command)

        if handled:
            self.say(message)
            name = self.listener.listen()
            learn_folder(name)
            return True

        handled, message = learn_app_confirmer(command)

        if handled:
            self.say(message)
            name = self.listener.listen()
            learn_app(name)
            return True
        return False
    
    def handle_system(self, command):
        handled, message = shutdown_confirmation(command)

        if handled:
            self.say(message)
            confirmation = self.listener.listen()
            shutdown(confirmation)
            return True
        
        handled, message = restart_confirmation(command)

        if handled:
            self.say(message)
            confirmation = self.listener.listen()
            restart(confirmation)
            return True
        
        handled, message = log_out_confirmation(command)

        if handled:
            self.say(message)
            confirmation = self.listener.listen()
            log_out(confirmation)
            return True
        
        handled, message = lock(command)

        if handled:
            self.say(message)
            return True
        
        handled, message = sleep(command)

        if handled:
            self.say(message)
            return True
            
        handled, message = hibernate(command)

        if handled:
            self.say(message)
            return True

        return False

    def unknown_command(self):
        self.say("sorry. i don't know that command.", dashboard.Dashboard.BOT)


    def execute(self, command):
        if self.handle_opening(command):
            return
        
        if self.handle_learning(command):
            return
        
        if self.handle_system(command):
            return
        
        self.unknown_command()
