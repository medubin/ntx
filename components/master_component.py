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


    
    def render(self):
        self.files = Files(self.store).render()

        self.header = Header(self.store).render()
        self.open_file = OpenFile(self.store).render()
        self.input_bar = InputBar(self.store).render()
        columns = urwid.Columns([self.files, urwid.Filler(self.open_file)])

        return urwid.Frame(columns, self.header, self.input_bar)

    def run(self, master_input_listener):
        self.master_input_listener = master_input_listener

        self.loop = urwid.MainLoop(
            self.render(), 
            self.palette, 
            input_filter=self.__input_filter,
            unhandled_input=self.master_input_listener.listen)
        self.loop.run()

    def __input_filter(self, input, raw):
        return input

        
