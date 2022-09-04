import json
import sqlite3
if __name__ == "__main__":
    import config
else:
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
    db_Path = config.resource_path('data/database.db')

    connection = sqlite3.connect(db_Path)
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS clients (id INTEGER, name VARCHAR(30), last_name VARCHAR(30))')

    connection = sqlite3.connect(db_Path)
    cursor = connection.cursor()
    cursor.execute( 'SELECT * FROM clients')

    for row in cursor.fetchall():
        client = Client(id=row[0], name=row[1], lastName=row[2])
        db.append(client)
    
    connection.commit()
    connection.close()



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
        
        connection = sqlite3.connect(Clients.db_Path)
        cursor = connection.cursor()
        cursor.execute("Delete from clients")

        for client in Clients.db:
            cursor.execute( f"INSERT INTO clients Values ('{client.id}','{client.name}','{client.lastName}')")


        connection.commit()

        connection.close()

