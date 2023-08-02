from __future__ import annotations
from threading import *
import tkinter as tk
from tkinter import LEFT
from tkinter import scrolledtext


class Gui:
    def __init__(self, window, chatgpt) -> None:
        self.chatgpt = chatgpt
        window.title("TTS")
        # Textbox to display the conversation
        self.text_box = scrolledtext.ScrolledText(
            window, wrap=tk.WORD, width=80, height=20
        )
        self.text_box.pack(padx=10, pady=10)
        self.text_box.insert(tk.END, "AI: Hello! How can I assist you?\n")

        # Entry widget for user input
        self.user_input = tk.Entry(window, width=80)
        self.user_input.pack(padx=10, pady=5)

        # Send button to send user input
        self.send_button = tk.Button(window, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        self.window = window
        window.mainloop()

    def send_message(self):
        user_text = self.user_input.get()
        self.text_box.insert(tk.END, "USER: " + user_text + "\n")
        response = self.chatgpt.send_message(user_text)
        self.text_box.insert(tk.END, "AI: " + response + "\n")
        print("AI:", response)
