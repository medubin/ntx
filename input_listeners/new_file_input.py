from constants.input import Input
class NewFileInput:
    def __init__(self, store, service, components):
        self.store = store
        self.service = service
        self.components = components

    def listen(self, input, state):
        if state != self.store.STATE_NEW:
            return

        if input == 'enter':
            self.store.write_buffer = self.components.input_bar.get_edit_text()
            self.service.directory_service.create_new_note()
            self.components.input_bar.set_edit_text('')