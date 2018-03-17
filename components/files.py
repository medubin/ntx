import urwid
class Files:
    def __init__(self, store):
        self.store = store

    def render(self):
        contents = []
        for file in self.store.files:
            content = urwid.Text(file)
            contents.append(urwid.AttrMap(content, None, 'reveal focus'))
         
        listbox = urwid.ListBox(urwid.SimpleFocusListWalker(contents))
        listbox.set_focus(0)
        return listbox

