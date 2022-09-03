import json
import sqlite3
from scripts import config

class Client:

    def __init__(self, id, name, lastName):
        self.id = id
        self.name = name
        self.lastName = lastName

    def __str__(self):
        return f"[{self.id}] {self.name} {self.lastName}"


class Clients:

    db = []
    with open(config.DATABASE_PATH, newline= '\n') as csvfile:
        reader = csv.reader(csvfile,delimiter= ';')
        for id, name, lastName in reader:
            client = Client(id, name, lastName)
            db.append(client)
    # _db_json = open('data/db.json','a+')  # ?Fichero .Json


    @staticmethod
    def find(id):
        for client in Clients.db:
            if client.id == id:
                return client
    
    @staticmethod
    def create(id, name, lastName):
        client = Client(id, name, lastName)
        Clients.db.append(client)
        Clients.save()
        return client

    @staticmethod
    def modify(id, name, lastName):
        for index, client in enumerate(Clients.db):
            if client.id == id:
                Clients.db[index].name = name
                Clients.db[index].lastName = lastName
                Clients.save()
                return Clients.db[index] 
    
    @staticmethod
    def delete(id):
        for index, client in enumerate(Clients.db):
            if client.id == id:
                client = Clients.db.pop(index)
                Clients.save()

                return client

    @staticmethod
    def save():
        pass

    #?=============================.JSON=============================     
    # def _update():
    #     data = {}
    #     data['clients'] = []
    #     for client in Clients.db:
    #         data['clients'].append({'id':client.id,'name':client.name,'lastName':client.lastName})
    #     json.dump(data , Clients._db_json, indent = 4)
    #?===============================================================     
    