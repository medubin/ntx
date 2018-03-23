class NewFileInput:
    def __init__(self, env):
        self.env = env

    def listen(self, input, state):
        if state not in (self.env.store.STATE_NEW_FILE, self.env.store.STATE_NEW_FOLDER):
            return

        if self.__is_title_character(input):
            self.env.store.write_buffer += input
            self.env.component.input_bar.set_text(self.env.store.write_buffer)
        elif input == 'backspace':
            self.env.store.write_buffer = self.env.store.write_buffer[:-1]
            self.env.component.input_bar.set_text(self.env.store.write_buffer)
        elif input == 'enter':
            if self.env.store.state == self.env.store.STATE_NEW_FILE:
                filepath = self.env.store.full_directory() + '/' + self.env.store.write_buffer + ".md"
                self.env.service.create.note(filepath)
            elif self.env.store.state == self.env.store.STATE_NEW_FOLDER:
                folderpath = self.env.store.full_directory() + '/' + self.env.store.write_buffer
                self.env.service.create.folder(folderpath)
        elif input == 'esc':
            self.env.service.state.set_to_browse()

    
    def __is_title_character(self, input):
        if len(input) != 1:
            return False
        return (
            input.isalpha() or
            input.isdigit() or
            input in [' ', '-', '_', '.']
        )
    