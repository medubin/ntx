from base.base_service import BaseService

class InputService(BaseService):
    def push(self, input):
        self.store.push_write_buffer(input)
        self.component.input_bar.set_text(self.store.get_write_buffer())
    
    def pop(self):
        self.store.pop_write_buffer()
        self.component.input_bar.set_text(self.store.get_write_buffer())

    def is_title_character(self, input):
        if len(input) != 1:
            return False
        return (
            input.isalpha() or
            input.isdigit() or
            input in [' ', '-', '_', '.']
        )
    