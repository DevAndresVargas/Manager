from scripts import helpers
from scripts import database as db

def init():
    while True:
        
        helpers.clear_screen()

        print("""
        =============================
            Welcome to the Manager
        =============================
        [1] List clients
        [2] Find client
        [3] Add client
        [4] Modify client
        [5] Delete client
        [6] Close Manager
        =============================        
        """)

        option = int(input('> '))

        helpers.clear_screen()

        match option:
            case 1:
                print('Listing clients...\n')
                for client in db.Clients.db:
                    print(client)

            case 2:
                print('Search client...\n')
                id = helpers.read_text(3,3,"ID (1 char - 2 int)").upper()
                client = db.Clients.find(id)
                print(client) if client else print("Client not find")
            case 3:
                print('Adding client...\n')
                id = helpers.read_text(3, 3, "ID (1 char - 2 int)").upper()
                name = helpers.read_text(3, 30, "Name (3-30 char)").capitalize()
                lastName = helpers.read_text(3, 30, "LastName (3-30 charss)").capitalize()
                client = db.Clients.create(id, name, lastName)
                print("Client Created")

            case 4:
                print('Modifying client...\n')
                id = helpers.read_text(3,3,"ID (1 char - 2 int)").upper()
                client = db.Clients.find(id)

                if client:
                    name = helpers.read_text(3, 30,f"New Name(3-30 chars) OldName[{client.name}]")
                    lastName = helpers.read_text(3, 30,f"New LastName(3-30 chars) OldLastName[{client.lastName}]")
                    db.Clients.modify(id, name, lastName)

            case 5: 
                print('Deleting client...\n')
                for client in db.Clients.db:
                    print(client)
                print("=============================\n")
                id = helpers.read_text(3,3,"ID (1 char - 2 int)").upper()
                client = db.Clients.delete(id)

                if client:
                    print(f"Client: [{client.id}] {client.name} {client.lastName} delete succesfull...")

                # TODO
            case 6:
                print('Exit...\n')
                db.Clients._update()
                break
        input("\nPress Enter to continue...")
        
    
    input("\nPress Enter to continue...")
            
        