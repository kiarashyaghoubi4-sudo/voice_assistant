import customtkinter as ctk
from utils.paths import ASSETS
class Dashboard:

    IDLE = "💤 Idle"
    LISTENING = "🎤 Listening..."
    THINKING = "🧠 Thinking..."
    SPEAKING = "🔊 Speaking..."
    BOT = "🤖"
    USER ="👤"

    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("350x300")
        self.window.title("Voice Assistant")
        self.window.iconbitmap(ASSETS / "icon.ico")
        self.create_widgets()
        self.create_labels()
        self.create_chat_box()

    def create_widgets(self):
        self.header_frame = ctk.CTkFrame(self.window, height=60)
        self.header_frame.pack(fill="x")

        self.chat_frame = ctk.CTkFrame(self.window)
        self.chat_frame.pack(fill="both", expand=True)

        self.footer_frame = ctk.CTkFrame(self.window, height=100)
        self.footer_frame.pack(fill="x")

    def create_labels(self):
        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="🤖 Voice Assistant",
            font=("Segoe UI", 20, "bold")
            )
        self.title_label.pack( pady = 15)

        self.status_label = ctk.CTkLabel(self.header_frame, text=Dashboard.IDLE, font=("Segoe UI", 15, "bold"))
        self.status_label.pack(pady = 25)

    def set_status(self, status):
        self.status_label.configure(text = status)
        self.window.update_idletasks()


    def create_chat_box(self):
        self.chat_box = ctk.CTkTextbox(self.chat_frame)
        self.chat_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )
        self.chat_box.configure(state="disabled")

    def show_msg(self, msg, sender):
        self.chat_box.configure(state="normal")

        self.chat_box.insert("end", f"{sender}: {msg}\n\n")
        self.chat_box.see("end")

        self.chat_box.configure(state="disabled")

    def destroy_window(self):
        self.window.destroy()

    def start_window(self):
        self.window.mainloop()
