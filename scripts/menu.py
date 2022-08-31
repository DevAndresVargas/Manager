import helpers
import database as db

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
                for client in db.Clients.toList:
                    print(client)
            case 2:
                print('Search client...\n')
                id = helpers.read_text(3,3,"ID (2 int y 1 char)").upper()
                client = db.Clients.find(id)
                print(client) if client else print("Client not find")
            case 3:
                print('Adding client...\n')
                id = helpers.read_text(3, 3, "ID (2 int - 1 char)").upper()
                name = helpers.read_text(5, 30, "Name (5-30 char)").capitalize()
                lastName = helpers.read_text(5, 30, "LastName (5-30 charss)").capitalize()
                client = db.Clients.create(id, name, lastName)
                print("Client Created")

            case 4:
                print('Modifying client...\n')
                id = helpers.read_text(3,3,"ID (2 int - 1 char)").upper()
                client = db.Clients.find(id)

                if client:
                    name = helpers.read_text(5, 30,f"New Name(5-30 chars) OldName[{client.name}]")
                    lastName = helpers.read_text(5, 30,f"New LastName(5-30 chars) OldLastName[{client.lastName}]")

            case 5:
                print('Deleting client...\n')
                # TODO
            case 6:
                print('Exit...\n')
                break
        
    
    input("\n Press Enter to continue...")
            
        