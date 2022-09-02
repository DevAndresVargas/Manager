from scripts import menu
from scripts import ui
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        menu.init()
    else:
        app = ui.MainWindow()
        app.mainloop()