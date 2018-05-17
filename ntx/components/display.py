import urwid
from ntx.base.base_component import BaseComponent
class Display(BaseComponent):
    def __init__(self, env):
        self.env = env
        self.__text = ''
        self.widget = self.__render()


    def __render(self):
        return urwid.Text(self.get_text())


    # Setters and Getters    

    def set_text(self, text):
        self.__text = text
        self.widget.set_text(self.__text or '')


    def get_text(self):
        return self.__text

    

    
    