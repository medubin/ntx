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
            self.service.command.interpret(self.component.input.get_text())
        elif input == 'left':
            self.service.input.change_write_cursor_pos(1)
        elif input == 'right':
            self.service.input.change_write_cursor_pos(-1)
        elif input == 'esc':
            self.service.state.browse()
        elif input == 'tab':
            self.service.command.autocomplete(self.component.input.get_text())


    
