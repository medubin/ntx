from constants.state import State
from base.base_input import BaseInput
class NewFileInput(BaseInput):
    def listen(self, input, state):
        if state not in (State.NEW_FILE, State.NEW_FOLDER):
            return

        if self.service.input.is_title_character(input):
            self.service.input.push(input)
        elif input == 'backspace':
            self.service.input.pop()
        elif input == 'enter':
             full_path = self.store.full_directory() + '/' + self.store.write_buffer
             self.service.create.folder_or_note(full_path)
        elif input == 'esc':
            self.service.state.set_to_browse()

    
