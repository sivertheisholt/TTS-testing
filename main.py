import tkinter as tk
from gpt_api import GptApi

from gui import Gui

API_KEY = ""
API_URL = "https://api.openai.com/v1/chat/completions"

chatbot = GptApi(API_KEY, API_URL)

window = tk.Tk()
main_ui = Gui(window, chatbot)
