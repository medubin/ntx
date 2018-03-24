from constants.state import State
from base.base_input import BaseInput
class SearchResultInput(BaseInput):
    def listen(self, input, state):
        if state != State.SEARCH_RESULT:
            return

        if input == 'up':
            self.service.directory.scroll(-1)
        elif input == 'down':
            self.service.directory.scroll(1)
        elif input == 'enter' or input == 'right':
            file = self.store.search_results[self.store.selected_file]
            self.service.editor.edit_file(file)
        elif input == 'esc':
            self.service.state.browse()
  
