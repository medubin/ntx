from constants.state import State
from base.base_input import BaseInput
class SearchInput(BaseInput):
    def listen(self, input, state):
        if state != State.SEARCH_INPUT:
            return
        if len(input) == 1:
            self.service.input.push(input)
        elif input == 'backspace':
            self.service.input.pop()
        elif input == 'enter':
            self.service.search.search(self.store.write_buffer)
            self.service.state.search_results()
        elif input == 'esc':
            self.service.state.browse()