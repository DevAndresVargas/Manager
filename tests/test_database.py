import unittest
import copy
from scripts import database as db


class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clients.db = [
            db.Client('x54', 'Carlos', 'Ruiz'),
            db.Client('j35', 'Ricardo', 'Ruiz'),
            db.Client('x27', 'Ana', 'Lozano')
        ]
    
    def test_find_client(self):
        client_existing = db.Clients.find('x27')
        client_not_existing = db.Clients.find('j34')

        self.assertIsNotNone(client_existing)
        self.assertIsNone(client_not_existing)
    
    def test_create_client(self):
        new_client = db.Clients.create('x40', 'Camila', 'Lozano')
        self.assertEqual(new_client.name,'Camila')
        self.assertEqual(new_client.lastName,'Lozano')
        self.assertEqual(new_client.id,'x40')

    def test_modify_client(self):
        client_to_modify = copy.copy(db.Clients.find('j35'))
        client_modified = db.Clients.modify('j35','Luis','Ruiz')
        self.assertEqual(client_to_modify.name,'Ricardo')
        self.assertEqual(client_modified.name,'Luis')

    def test_delete_client(self):
        client_deleted = db.Clients.delete('x27')
        client_Refind = db.Clients.find('x27')
        self.assertEqual(client_deleted.id,'x27')
        self.assertIsNone(client_Refind)