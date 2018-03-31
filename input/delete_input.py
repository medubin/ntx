from constants.state import State
from base.base_input import BaseInput

class DeleteInput(BaseInput):
    def listen(self, input, state):
        if state != State.DELETE:
            return
        
        if input in ['Y', 'n'] and not len(self.store.get_write_buffer()):
             self.service.input.push(input)
        elif input == 'backspace':
            self.service.input.pop()
        elif input == 'enter':
            if (self.store.get_write_buffer() == 'Y'):
                full_path = self.store.get_full_directory() + '/' + self.store.selected_file_name()
                self.service.delete.folder_or_note(full_path)

            self.service.state.browse()

