from constants.input import Input
class NewFileInput:
    def __init__(self, store, term, service):
        self.store = store
        self.term = term
        self.service = service

    def listen(self, input, state):
        if state != self.store.STATE_NEW:
            return
        
        if input[0].isalpha() or input[0].isdigit():
            self.store.write_buffer += input[0]
        elif input == Input.DELETE:
            self.store.write_buffer = self.store.write_buffer[:-1]
        elif input == Input.ENTER:
            self.service.directory_service.create_new_note()