from constants.state import State
from base.base_input import BaseInput
class CommandInput(BaseInput):
    def listen(self, input, state):
        if state != State.COMMAND:
            return

        if self.service.input.is_title_character(input):
            self.service.input.insert(input)
        elif input == 'backspace':
            self.service.input.splice()
        elif input == 'enter':
            self.service.command.interpret(self.store.get_write_buffer())
        elif input == 'left':
            self.service.input.change_write_cursor_pos(1)
        elif input == 'right':
            self.service.input.change_write_cursor_pos(-1)
        elif input == 'esc':
            self.service.state.browse()

    
