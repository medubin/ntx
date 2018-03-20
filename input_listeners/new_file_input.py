from constants.input import Input
class NewFileInput:
    def __init__(self, store, service, components):
        self.store = store
        self.service = service
        self.components = components

    def listen(self, input, state):
        if state != self.store.STATE_NEW:
            return

        if self.__is_title_character(input):
            self.store.write_buffer += input
            self.components.input_bar.widget.set_text(self.store.write_buffer)
        elif input == 'backspace':
            self.store.write_buffer = self.store.write_buffer[:-1]
            self.components.input_bar.widget.set_text(self.store.write_buffer)
        elif input == 'enter':
            self.service.directory_service.create_new_note()
            self.components.input_bar.widget.set_text('')
            self.components.files.content[:] = self.components.files.create_files()
        elif input == 'esc':
            self.components.input_bar.widget.set_text('')
            self.store.state = self.store.STATE_BROWSE

    
    def __is_title_character(self, input):
        if len(input) != 1:
            return False
        return (
            input.isalpha() or
            input.isdigit() or
            input in [' ', '-', '_', '.']
        )
    