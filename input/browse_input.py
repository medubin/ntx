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
            self.env.service.directory.view_file_or_folder()
        elif input == 'e':
            self.env.service.editor.edit_file()
        elif input == 'left':
            self.env.service.directory.leave_folder()

    def scroll_up(self):
        if self.env.store.selected_file > 0:
            self.env.store.selected_file -= 1 
            self.env.component.files.widget.focus_position = self.env.store.selected_file

    def scroll_down(self):
        if self.env.store.selected_file < len(self.env.store.files) - 1:
            self.env.store.selected_file += 1
            self.env.component.files.widget.focus_position = self.env.store.selected_file
