import urwid
class Header:
    def __init__(self, store):
        self.store = store
        self.widget = self.__render()
    
    def __render(self):
        header_text = urwid.Text("ntx", wrap='clip')
        return urwid.AttrMap(header_text, 'header')
