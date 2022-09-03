import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys.__MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
    
    

DATABASE_PATH = resource_path('data/clients.csv')

if 'pytest' in sys.argv[0]:
    DATABASE_PATH = resource_path('tests/clients_test.csv')