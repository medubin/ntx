from constants.state import State
from base.base_input import BaseInput
class CommandInput(BaseInput):
    def listen(self, input, state):
        if state != State.COMMAND:
            return

        if self.service.input.is_title_character(input):
            self.service.input.push(input)
        elif input == 'backspace':
            self.service.input.pop()
        elif input == 'enter':
            self.service.command.interpret(self.store.get_write_buffer())
        elif input == 'esc':
            self.service.state.browse()

    
