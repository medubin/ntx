import urwid
import os
from base.base_component import BaseComponent

class Files(BaseComponent):
    def __init__(self, env):
        self.env = env
        self.content = urwid.SimpleFocusListWalker(self.create_files(self.env.store.get_files()))
        self.widget = self.__render()
        

    def __render(self):
        listbox = ListBoxOverride(self.content)
        if len(self.content):
            listbox.set_focus(0)
        return listbox

    def create_files(self, files):
        contents = []
        for file in files:
            full_path = self.env.store.get_full_directory() + '/' + file
            content = urwid.Text(file)
            if os.path.isdir(full_path):
                contents.append(urwid.AttrMap(content, 'folder', 'reveal focus'))
            else:
                contents.append(urwid.AttrMap(content, None, 'reveal focus'))

        return contents
    
    def set_focus(self, focus):
        if len(self.content):
            self.widget.set_focus(focus)

# overrides the keypress which has some weird behavior in urwid.
class ListBoxOverride(urwid.ListBox):
    def keypress(self, size, key):
        return key