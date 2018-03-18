import pager
from constants.input import Input
import urwid
class BrowseInput:
    def __init__(self, store, service, components):
        self.store = store
        self.service = service
        self.components = components

    def listen(self, input, state):
        if state != self.store.STATE_BROWSE:
            return
        if input == 'up':
            self.scroll_up()
        elif input == 'down':
            self.scroll_down()
        elif input == 'n':
            self.store.state = self.store.STATE_NEW  
            # self.components.input_bar.set_edit_pos(0)  
        elif input == 'enter':
            self.view_file()
        elif input == 'e':
            self.service.editor_service.open_selected_file()
            self.view_file()

    def scroll_up(self):
        if self.store.selected_file > 0:
            self.store.selected_file -= 1 
            self.components.files.focus_position = self.store.selected_file

    def scroll_down(self):
        if self.store.selected_file < len(self.store.files) - 1:
            self.store.selected_file += 1
            self.components.files.focus_position = self.store.selected_file

    def view_file(self):
        file = self.service.directory_service.get_selected_file()
        if (file is not None):
            self.store.opened_file = self.service.directory_service.get_file_contents(file)
            self.components.open_file.set_text(self.store.opened_file)