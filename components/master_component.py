import urwid

from components.files import Files
from components.input_bar import InputBar
from components.open_file import OpenFile
from components.header import Header

class MasterComponent:
    palette = [('header', 'light green', 'dark blue'),
    ('reveal focus', 'black', 'dark cyan', 'standout')]
    def __init__(self, env):
        self.env = env
        self.files = Files(self.env)
        self.header = Header(self.env)
        self.input_bar = InputBar(self.env)
        self.open_file = OpenFile(self.env)
    
    def render(self):
        columns = urwid.Columns([self.files.widget, urwid.Filler(self.open_file.widget)])
        return urwid.Frame(columns, self.header.widget, self.input_bar.widget)

    def run(self):

        self.loop = urwid.MainLoop(
            self.render(), 
            self.palette, 
            input_filter=self.__input_filter,
            unhandled_input=self.env.input.listen)
        self.loop.run()

    def __input_filter(self, input, raw):
        return input

        
