import urwid

from components.files import Files
from components.input_bar import InputBar
from components.open_file import OpenFile
from components.header import Header

class MasterComponent:
    palette = [('header', 'light green', 'dark blue'),
    ('reveal focus', 'black', 'dark cyan', 'standout'),
    ('input', 'light green', 'black' ),
    ('input cursor', 'light green', 'white', 'blink'),
    ('folder', 'light green', '', 'bold')
    ]

    def __init__(self, env):
        self.env = env
        self.files = Files(self.env)
        self.header = Header(self.env)
        self.input_bar = InputBar(self.env)
        self.open_file = OpenFile(self.env)
    
    # def setup(self):
    #     self.files.setup()
    #     self.header.setup()
    #     self.input_bar.setup()
    #     self.open_file.setup()
    
    def render(self):
        columns = urwid.Columns([self.files.widget, urwid.Filler(self.open_file.widget, valign='top')])
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

        
