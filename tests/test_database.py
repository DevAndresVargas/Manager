import unittest
import copy
import csv
from scripts import database as db
from scripts import helpers,config


class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clients.db = [
            db.Client('xs3', 'Carlos', 'Ruiz'),
            db.Client('sf8', 'Ricardo', 'Ruiz'),
            db.Client('xd2', 'Ana', 'Lozano')
        ]
    
    def test_find_client(self):
        client_existing = db.Clients.find('xd2')
        client_not_existing = db.Clients.find('j34')

        self.assertIsNotNone(client_existing)
        self.assertIsNone(client_not_existing)
    
    def test_create_client(self):
        new_client = db.Clients.create('x40', 'Camila', 'Lozano')
        self.assertEqual(new_client.name,'Camila')
        self.assertEqual(new_client.lastName,'Lozano')
        self.assertEqual(new_client.id,'x40')

    def test_modify_client(self):
        client_to_modify = copy.copy(db.Clients.find('sf8'))
        client_modified = db.Clients.modify('sf8','Luis','Ruiz')
        self.assertEqual(client_to_modify.name,'Ricardo')
        self.assertEqual(client_modified.name,'Luis')

    def test_delete_client(self):
        client_deleted = db.Clients.delete('xd2')
        client_Refind = db.Clients.find('xd2')
        self.assertEqual(client_deleted.id,'xd2')
        self.assertIsNone(client_Refind)

    def test_id_valid(self):
        self.assertTrue(helpers.id_valid("JJ2", db.Clients.db))

    def test_write_csv(self):
        db.Clients.delete('xs3')
        db.Clients.delete('sf8')
        db.Clients.modify('xd2', 'Anita', 'Ruiz')

        id, name, lastName = None, None, None
        with open(config.DATABASE_PATH, newline = '\n') as csvfile:
            reader = csv.reader(csvfile, delimiter = ';')
            id, name, lastName = next(reader)

        self.assertEqual(id, 'xd2')
        self.assertEqual(name, 'Anita')
        self.assertEqual(lastName, 'Ruiz')



