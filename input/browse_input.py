from constants.state import State
from base.base_input import BaseInput

class BrowseInput(BaseInput):
    def listen(self, input, state):
        if state != State.BROWSE:
            return
        if input == 'up':
            self.service.directory.scroll(-1)
            full_path = self.store.get_full_directory() + '/' + self.store.selected_file_name() 
            self.service.content.view(full_path)
        elif input == 'down':
            self.service.directory.scroll(1)
            full_path = self.store.get_full_directory() + '/' + self.store.selected_file_name() 
            self.service.content.view(full_path)
        elif input == 'enter' or input == 'right':
            self.service.content.open()
        elif input == 'left':
            self.service.folder_content.close()
        # elif input == 'n':
        #     self.service.state.new_note()
        # elif input == 'N':
        #     self.service.state.new_folder()
        # elif input == 'g':
        #     self.service.state.search()
        # elif input == 'd':
        #     self.service.state.delete()
        elif input == 'i':
            self.service.state.command()
        elif input[0] == 'mouse press':
            if input[1] == 4.0:
                self.service.directory.scroll(-1)
            elif input[1] == 5.0:
                self.service.directory.scroll(1)

            