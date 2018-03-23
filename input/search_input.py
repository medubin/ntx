from constants.state import State

class SearchInput:
    def __init__(self, env):
        self.env = env

    def listen(self, input, state):
        if state != State.SEARCH_INPUT:
            return
        if len(input) == 1:
            self.env.store.write_buffer += input
            self.env.component.input_bar.set_text(self.env.store.write_buffer)
        elif input == 'backspace':
            self.env.store.write_buffer = self.env.store.write_buffer[:-1]
            self.env.component.input_bar.set_text(self.env.store.write_buffer)
        elif input == 'enter':
            self.env.service.search.search(self.env.store.write_buffer)
            self.env.service.state.search_results()
        elif input == 'esc':
            self.env.service.state.set_to_browse()