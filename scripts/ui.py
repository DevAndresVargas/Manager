from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel,WARNING,showinfo
from scripts import database as db
from scripts import helpers


class CenterWidgetMixin:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)
        self.geometry(f"{w}x{h}+{x}+{y}")  # *WIDTHxHEIGHT+OFFSET_X+OFFSET_Y


class CreateClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Create client")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()


    def build(self):
        frame = Frame(self)
        frame.pack(padx = 20, pady = 10)

        Label(frame, text = 'ID (2 upper chars and 1 int)').grid(row = 0,column = 0)
        Label(frame, text = 'Name (3 - 30 chars)').grid(row = 0,column = 1)
        Label(frame, text = 'LastName (3 - 30 chars)').grid(row = 0,column = 2)

        id = Entry(frame)
        id.grid(row = 1, column = 0)
        id.bind('<KeyRelease>', lambda event: self.validate(event, 0))

        name = Entry(frame)
        name.grid(row = 1, column = 1)
        name.bind('<KeyRelease>', lambda event: self.validate(event, 1))


        lastName = Entry(frame)
        lastName.grid(row = 1, column = 2)
        lastName.bind('<KeyRelease>', lambda event: self.validate(event, 2))


        frame = Frame(self)
        frame.pack(pady = 10)

        create = Button(frame, text = "Create", command = self.create_client)
        create.configure(state = DISABLED)
        create.grid(row = 0, column = 0)
        Button(frame, text = "Cancel", command = self.close).grid(row = 0, column = 1)

        self.validations = [False,False,False]
        self.create = create
        self.id = id
        self.name = name
        self.lastName = lastName

    def create_client(self):
        self.master.treeview.insert(
                        parent= '', index='end', iid = self.id.get().upper(),
                        values=(self.id.get(), self.name.get(), self.lastName.get())
                    )
        db.Clients.create(self.id.get(), self.name.get(), self.lastName.get())
        self.close()
    
    
    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        value = event.widget.get()
        valid = helpers.id_valid( value, db.Clients.db) if index == 0 \
            else (value.isalpha() and len(value) > 3 and len(value) <= 30)
        event.widget.configure({'bg': 'Green' if valid else 'Red'})

        self.validations[index] = valid
        self.create.config(state=NORMAL if self.validations == [1,1,1] else DISABLED)


class EditClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Edit client")
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()


    def build(self):
        frame = Frame(self)
        frame.pack(padx = 20, pady = 10)

        Label(frame, text = 'ID (not editable)').grid(row = 0,column = 0)
        Label(frame, text = 'Name (3 - 30 chars)').grid(row = 0,column = 1)
        Label(frame, text = 'LastName (3 - 30 chars)').grid(row = 0,column = 2)

        id = Entry(frame)
        id.grid(row = 1, column = 0)

        name = Entry(frame)
        name.grid(row = 1, column = 1)
        name.bind('<KeyRelease>', lambda event: self.validate(event, 0))

        lastName = Entry(frame)
        lastName.grid(row = 1, column = 2)
        lastName.bind('<KeyRelease>', lambda event: self.validate(event, 1))

        client = self.master.treeview.focus()
        fields = self.master.treeview.item(client, 'values')

        id.insert(0, fields[0])
        id.config(state = DISABLED)
        name.insert(0, fields[1])
        lastName.insert(0, fields[2])

        frame = Frame(self)
        frame.pack(pady = 10)

        update_client = Button(frame, text = "Edit", command = self.update_client)
        update_client.grid(row = 0, column = 0)
        Button(frame, text = "Cancel", command = self.close).grid(row = 0, column = 1)

        self.validations = [1,1]
        self.updaupdate_client =update_client
        self.id = id
        self.name = name
        self.lastName = lastName

    def update_client(self):
        client = self.master.treeview.focus()
        self.master.treeview.item(client, values=(
                self.id.get(), self.name.get(), self.lastName.get()))
        db.Clients.modify(self.id.get(), self.name.get(), self.lastName.get())
        self.close()
    
    
    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        value = event.widget.get()
        valid = (value.isalpha() and len(value) > 3 and len(value) <= 30)
        event.widget.configure({'bg': 'Green' if valid else 'Red'})

        self.validations[index] = valid
        self.update_client.config(state=NORMAL if self.validations == [1,1] else DISABLED)

"""

        *This form is functional but can be trimmed using ternary operators
        
        match index:
            case 0:
                valid = helpers.id_valid(value, db.Clients.db)
                if valid:
                    event.widget.configure({'bg': 'Green'})
                else:
                    event.widget.configure({'bg': 'Red'})

            case 1:
                valid = value.isalpha() and len(value) > 3 and len(value) <= 30
                if valid:
                    event.widget.configure({'bg': 'Green'})
                else:
                    event.widget.configure({'bg': 'Red'})
            
            case 2:
                valid = value.isalpha() and len(value) > 3 and len(value) <= 30
                if valid:
                    event.widget.configure({'bg': 'Green'})
                else:
                    event.widget.configure({'bg': 'Red'})

"""



class MainWindow(Tk,CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("Clients Manager")
        self.build()
        self.center()


    def build(self):
        frame = Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('ID', 'NAME', 'LASTNAME')

        treeview.column('#0', width= 0, stretch=NO)
        treeview.column('ID', anchor=CENTER)
        treeview.column('NAME', anchor=CENTER)
        treeview.column('LASTNAME', anchor=CENTER)

        treeview.heading('ID', text='ID', anchor=CENTER)
        treeview.heading('NAME', text='NAME', anchor=CENTER)
        treeview.heading('LASTNAME', text='LASTNAME', anchor=CENTER)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side = RIGHT, fill=Y)
        treeview['yscrollcommand'] = scrollbar.set

        for client in db.Clients.db:
                    treeview.insert(
                        parent= '', index='end', iid = client.id,
                        values=(client.id, client.name, client.lastName)
                    )

        treeview.pack()

        frame = Frame(self)
        frame.pack(pady = 20)
        
        Button(frame, text= 'Create', command = self.create).grid(row = 0, column = 0)
        Button(frame, text= 'Modify', command = self.edit).grid(row = 0, column = 1)
        Button(frame, text= 'Delete', command = self.delete).grid(row = 0, column = 2)

        self.treeview = treeview

    def delete(self):
        client = self.treeview.focus()
        
        if client:
            fields = self.treeview.item(client,"values")
            confirm = askokcancel(
                title= "confirm delete",
                message = f"Delete {fields[1]} {fields[2]}?",
                icon = WARNING)
            if confirm:
                self.treeview.delete(client)
                db.Clients.delete(fields[0])

    def create(self):
        CreateClientWindow(self)
    
    def edit(self):
        if self.treeview.focus():
            EditClientWindow(self)
        else:
            showinfo(message = 'No client selected', title = 'No client')
    

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()