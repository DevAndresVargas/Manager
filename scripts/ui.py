from tkinter import *
from tkinter import ttk
import database as db

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


        treeview.pack()

        frame = Frame(self)
        frame.pack(pady = 20)
        
        button

        for client in db.Clients.db:
            treeview.insert(
                parent= '', index='end', iid = client.id,
                values=(client.id, client.name, client.lastName)
            )

        treeview.pack()

    def hi(self):
        print("hola mundo")

    


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()