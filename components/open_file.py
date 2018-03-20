import urwid
class OpenFile:
    def __init__(self, store):
        self.store = store
        self.widget = self.__render()

    def __render(self):
        return urwid.Text(self.store.opened_file)