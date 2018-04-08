import urwid

from components.navigation import Navigation
from components.input import Input
from components.display import Display
from components.header import Header
from constants.state import State

class MasterComponent:
    palette = [
    ('header', 'light green', 'dark blue'),
    ('reveal focus', 'black', 'dark cyan', 'standout'),
    ('input', 'light green', 'black' ),
    ('input cursor', 'light green', 'white', 'blink'),
    ('folder', 'light green', '', 'bold')
    ]

    def __init__(self, env):
        self.env = env
        self.__state = State.BROWSE 

        self.navigation = Navigation(self.env)
        self.header = Header(self.env)
        self.input = Input(self.env)
        self.display = Display(self.env)
    

    
    def render(self):
        columns = urwid.Columns([self.navigation.widget, urwid.Filler(self.display.widget, valign='top')])
        return urwid.Frame(columns, self.header.widget, self.input.widget)

    def run(self):
        self.loop = urwid.MainLoop(
            self.render(), 
            self.palette, 
            input_filter=self.__input_filter,
            unhandled_input=self.env.input.listen)

        self.loop.screen.set_terminal_properties(colors=256)
        self.loop.run()

    def __input_filter(self, input, raw):
        return input


    #Getters and Setters
    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state


        
