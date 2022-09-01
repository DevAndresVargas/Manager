import sys

DATABASE_PATH = 'data/clients.csv'

if 'pytest' in sys.argv[0]:
    DATABASE_PATH = 'tests/clients_test.csv'
