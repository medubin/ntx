import urwid
class Files:
    def __init__(self, store):
        self.store = store
        self.content = urwid.SimpleFocusListWalker(self.create_files())
        self.widget = self.__render()
        

    def __render(self):
        listbox = urwid.ListBox(self.content)
        listbox.set_focus(0)
        return listbox

    def create_files(self):
        contents = []
        for file in self.store.files:
            content = urwid.Text(file)
            contents.append(urwid.AttrMap(content, None, 'reveal focus'))
        return contents


