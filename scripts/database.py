import json

class Client:

    def __init__(self, id, name, lastName):
        self.id = id
        self.name = name
        self.lastName = lastName

    def __str__(self):
        return f"[{self.id}] {self.name} {self.lastName}"


class Clients:

    db = []
    _db_json = open('db.json','a+')

    @staticmethod
    def find(id):
        for client in Clients.db:
            if client.id == id:
                return client
    
    @staticmethod
    def create(id, name, lastName):
        client = Client(id, name, lastName)
        Clients.db.append(client)
        return client

    @staticmethod
    def modify(id, name, lastName):
        for index, client in enumerate(Clients.db):
            if client.id == id:
                Clients.db[index].name = name
                Clients.db[index].lastName = lastName
                return Clients.db[index] 
    
    @staticmethod
    def delete(id):
        for index, client in enumerate(Clients.db):
            if client.id == id:
                return Clients.db.pop(index)
                
    def _update():
        data = {}
        data['clients'] = []
        for client in Clients.db:
            data['clients'].append({'id':client.id,'name':client.name,'lastName':client.lastName})
        json.dump(data , Clients._db_json, indent = 4)
    