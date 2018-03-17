import urwid

from components.files import Files
from components.input_bar import InputBar
from components.open_file import OpenFile
from components.header import Header

class MasterComponent:
    palette = [('header', 'light green', 'dark blue'),
    ('reveal focus', 'black', 'dark cyan', 'standout')]
    def __init__(self, store):
        self.store = store

        self.files = Files(store).render()

        self.header = Header(store).render()
        self.open_file = OpenFile(store).render()
        self.input_bar = InputBar(store).render()


    
    def render(self):
        columns = urwid.Columns([self.files, urwid.Filler(self.open_file)])

        return urwid.Frame(columns, self.header, self.input_bar)
        
