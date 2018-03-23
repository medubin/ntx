from constants.state import State
from base.base_input import BaseInput

class BrowseInput(BaseInput):
    def listen(self, input, state):
        if state != State.BROWSE:
            return
        if input == 'up':
            self.service.directory.scroll(-1)
        elif input == 'down':
            self.service.directory.scroll(1)
        elif input == 'n':
            self.service.state.new_note()
        elif input == 'N':
            self.service.state.new_folder()
        elif input == 'enter' or input == 'right':
            self.service.content.open()
        elif input == 'left':
            self.service.folder_content.close()
        elif input == 'g':
            self.service.state.search()