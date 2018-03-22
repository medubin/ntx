import pager
from constants.input import Input
import urwid
class BrowseInput:
    def __init__(self, env):
        self.env = env

    def listen(self, input, state):
        if state != self.env.store.STATE_BROWSE:
            return
        if input == 'up':
            self.scroll_up()
        elif input == 'down':
            self.scroll_down()
        elif input == 'n':
            self.env.store.state = self.env.store.STATE_NEW_FILE
        elif input == 'f':
            self.env.store.state = self.env.store.STATE_NEW_FOLDER
        elif input == 'enter':
            self.view_file()
        elif input == 'e':
            self.env.service.editor.edit_file()

    def scroll_up(self):
        if self.env.store.selected_file > 0:
            self.env.store.selected_file -= 1 
            self.env.component.files.widget.focus_position = self.env.store.selected_file

    def scroll_down(self):
        if self.env.store.selected_file < len(self.env.store.files) - 1:
            self.env.store.selected_file += 1
            self.env.component.files.widget.focus_position = self.env.store.selected_file

    def view_file(self):
        file = self.env.service.directory.get_selected_file()
        if (file is not None):
            self.env.store.opened_file = self.env.service.file_content.get(file)
            self.env.component.open_file.widget.set_text(self.env.store.opened_file)