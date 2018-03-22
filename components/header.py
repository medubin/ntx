import urwid
class Header:
    def __init__(self, env):
        self.env = env
        self.widget = self.__render()
    
    def __render(self):
        header_text = urwid.Text("ntx", wrap='clip', align='center')
        return urwid.AttrMap(header_text, 'header')
