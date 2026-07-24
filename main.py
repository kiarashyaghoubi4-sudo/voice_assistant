from assistant import Assistant
from threading import Thread



assistant = Assistant()


assistant_thread = Thread(
    target=assistant.run,
    daemon=True
)
assistant_thread.start()
assistant.window.start_window()