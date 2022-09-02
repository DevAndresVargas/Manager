from tkinter import *
from tkinter import ttk

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
        treeview.pack()


    def hi(self):
        print("hola mundo")

    


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()