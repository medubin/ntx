import pager
from constants.input import Input
class BrowseInput:
    def __init__(self, store, term, service):
        self.store = store
        self.term = term
        self.service = service

    def listen(self, input, state):
        if state != self.store.STATE_BROWSE:
            return
        
        if input == pager.UP:
            self.scroll_up()
        elif input == pager.DOWN:
            self.scroll_down()
        elif input == ['n']:
            self.store.state = self.store.STATE_NEW    
        elif input == Input.ENTER:
            # self.service.markdown_service
            # print(self.store.files[self.store.selected_file])
            self.view_file()

    def scroll_up(self):
        if self.store.selected_file > -1:
            self.store.selected_file -= 1 

    def scroll_down(self):
        if self.store.selected_file < len(self.store.files) - 1:
            self.store.selected_file += 1

    def view_file(self):
        file = self.service.directory_service.get_selected_file()
        if (file is not None):
            self.store.opened_file = self.service.directory_service.get_file_contents(file)
