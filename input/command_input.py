from constants.state import State
import helpers.input_helper as input_helper

from base.base_input import BaseInput

class CommandInput(BaseInput):
    def listen(self, input, state):
        if state != State.COMMAND:
            return

        if input_helper.is_title_character(input):
            self.component.input.insert_char(input)
        elif input == 'backspace':
            self.component.input.splice_char()
        elif input == 'enter':
            self.service.command.interpret(self.component.input.get_text())
        elif input == 'left':
            self.component.input.scroll(1)
        elif input == 'right':
            self.component.input.scroll(-1)
        elif input == 'esc':
            self.service.state.browse()
        elif input == 'tab':
            self.service.command.autocomplete(self.component.input.get_text())


    
