import os
import platform

def clear_screen():
    os.system('cls') if platform.system() == 'Windows' else os.system('clear')

def read_text(min = 0, max = 100 ,message = None):
    print(message) if message else None
    while True:
        text = input('> ')
        if len(text) >= min and len(text) <= max:
            return text
