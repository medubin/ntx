import urwid
from base.base_component import BaseComponent
class Display(BaseComponent):
    def __init__(self, env):
        self.env = env
        self.__text = ''
        self.widget = self.__render()


    def __render(self):
        return urwid.Text(self.get_text())

    def set_display(self):
        self.widget.set_text(self.get_text())


    # Setters and Getters    

    def set_text(self, text):
        self.__text = text

    def get_text(self):
        return self.__text

    

    
    