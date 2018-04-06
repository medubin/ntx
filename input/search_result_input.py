from constants.state import State
from base.base_input import BaseInput
class SearchResultInput(BaseInput):
    def listen(self, input, state):
        if state != State.SEARCH_RESULT:
            return

        if input == 'up':
            self.service.directory.scroll(-1)
            full_path = self.store.BASE_DIRECTORY + '/' + self.store.search_results[self.store.get_file_index()]
            self.service.content.view(full_path)
        elif input == 'down':
            self.service.directory.scroll(1)
            full_path = self.store.BASE_DIRECTORY + '/' + self.store.search_results[self.store.get_file_index()]
            self.service.content.view(full_path)
        elif input == 'enter' or input == 'right':
            file = self.store.search_results[self.store.get_file_index()]
            full_path = self.store.BASE_DIRECTORY + '/' + file
            self.service.editor.edit_file(full_path)
        elif input == 'esc':
            self.store.pop_file_index()
            self.service.state.browse()
        
  
