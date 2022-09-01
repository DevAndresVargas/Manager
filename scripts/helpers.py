import os
import platform
import re

def clear_screen():
    os.system('cls') if platform.system() == 'Windows' else os.system('clear')

def read_text(min = 0, max = 100 ,message = None):
    print(message) if message else None
    while True:
        text = input('> ')
        if len(text) >= min and len(text) <= max:
            return text

def id_valid(id, list):
    if not re.match('[A-Z]{2}[0-9]$',id):
        print('Invalid ID, not meet the parameters')
        return False
    for client in list:
        if client.id == id:
            print("other client has this id")
            return False
    return True

