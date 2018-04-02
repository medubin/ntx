from base.base_service import BaseService

class InputService(BaseService):
    def push(self, input):
        self.store.push_write_buffer(input)
        self.component.input_bar.set_text(self.store.get_write_buffer())
    
    def pop(self):
        self.store.pop_write_buffer()
        self.component.input_bar.set_text(self.store.get_write_buffer())

    def insert(self, char):
        pos = len(self.store.get_write_buffer()) - self.store.get_write_cursor_pos()
        self.store.insert_write_buffer(char, pos)
        self.component.input_bar.set_text(self.store.get_write_buffer())
    
    def splice(self):
        pos = len(self.store.get_write_buffer()) - self.store.get_write_cursor_pos()
        self.store.splice_write_buffer(pos)
        self.component.input_bar.set_text(self.store.get_write_buffer())


    def is_title_character(self, input):
        if len(input) != 1:
            return False
        return (
            input.isalpha() or
            input.isdigit() or
            input in [' ', '-', '_', '.']
        )

    def change_write_cursor_pos(self, velocity):
        if 0 <= (self.store.get_write_cursor_pos() + velocity) <= len(self.store.get_write_buffer()):
            self.store.change_write_cursor_pos(velocity)
            self.component.input_bar.set_text(self.store.get_write_buffer())



    