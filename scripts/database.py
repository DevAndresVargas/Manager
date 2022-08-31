class Client:

    def __init__(self, id, name, lastName):
        self.id = id
        self.name = name
        self.lastName = lastName

    def __str__(self):
        return f"[{self.id}] {self.name} {self.lastName}"


class Clients:

    toList = []

    @staticmethod
    def find(id):
        for client in Clients.toList:
            if client.id == id:
                return client
    
    @staticmethod
    def create(id, name, lastName):
        client = Client(id, name, lastName)
        Clients.toList.append(client)
        return client

    @staticmethod
    def modify(id, name, lastName):
        for index, client in enumerate(Clients.toList):
            if client.id == id:
                Clients.toList[index].name = name
                Clients.toList[index].lastName = lastName
                return Clients.toList[index] 
    
    def delete(id):
        for index, client in enumerate(Clients.toList):
            if client.id == id:
                return Clients.toList.pop(index)
                

    