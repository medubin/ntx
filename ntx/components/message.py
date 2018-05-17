import urwid
from ntx.base.base_component import BaseComponent
from ntx.constants.messsage import Message as MessageConstant
class Message(BaseComponent):
    def __init__(self, env):
        self.env = env
        self.__text = MessageConstant.BASIC
        self.widget = self.__render()
        
    
    def __render(self):
        message_text = urwid.Text(self.__text, wrap='clip', align='center')
        return urwid.AttrWrap(message_text, 'message')

    # Setters and Getters    

    def set_text(self, text):
        self.__text = text
        self.widget.set_text(text)


    def get_text(self):
        return self.__text

    

    
    