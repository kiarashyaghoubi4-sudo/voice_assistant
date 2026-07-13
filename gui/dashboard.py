
import customtkinter as ctk

class Dashboard:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("300x200")
        self.window.title("Voice assistant")
        self.create_widgets()
        self.create_headers()
        self.create_chat_box()

    def create_widgets(self):
        self.header_frame = ctk.CTkFrame(self.window, height=60)
        self.header_frame.pack(fill="x")

        self.chat_frame = ctk.CTkFrame(self.window)
        self.chat_frame.pack(fill="both", expand=True)

        self.footer_frame = ctk.CTkFrame(self.window, height=70)
        self.footer_frame.pack(fill="x")

    def create_headers(self):
        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="🤖 Voice Assistant",
            font=("Segoe UI", 20, "bold")
            )
        self.title_label.pack( pady = 15)

    
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

        self.chat_box.insert("end", f"{sender}:\n    {msg}\n\n")
        self.chat_box.see("end")

        self.chat_box.configure(state="disabled")

    def start_window(self):
        self.window.mainloop()