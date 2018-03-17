import urwid
class OpenFile:
    def __init__(self, store):
        self.store = store

    def render(self):
        return urwid.Text(self.store.opened_file)