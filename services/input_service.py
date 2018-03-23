from base.base_service import BaseService

class InputService(BaseService):
    def push(self, input):
        self.store.write_buffer += input
        self.component.input_bar.set_text(self.store.write_buffer)
    
    def pop(self):
        self.store.write_buffer = self.store.write_buffer[:-1]
        self.component.input_bar.set_text(self.store.write_buffer)

    def is_title_character(self, input):
        if len(input) != 1:
            return False
        return (
            input.isalpha() or
            input.isdigit() or
            input in [' ', '-', '_', '.']
        )
    