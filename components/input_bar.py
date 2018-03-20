import urwid
class InputBar:
    def __init__(self, store):
        self.store = store
        self.widget = self.__render()

    def __render(self):
        return urwid.Text("")









