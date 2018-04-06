from base.base_service import BaseService

class InputService(BaseService):
    def push(self, input):
        self.component.input_bar.push_text(input)
        self.component.input_bar.set_display(self.component.input_bar.get_text())
    
    def pop(self):
        self.component.input_bar.pop_text()
        self.component.input_bar.set_display(self.component.input_bar.get_text())

    def insert(self, char):
        pos = len(self.component.input_bar.get_text()) -  self.component.input_bar.get_pos()
        self.component.input_bar.insert_text(char, pos)
        self.component.input_bar.set_display(self.component.input_bar.get_text())
    
    def splice(self):
        pos = len(self.component.input_bar.get_text()) - self.component.input_bar.get_pos()
        self.component.input_bar.splice_text(pos)
        self.component.input_bar.set_display(self.component.input_bar.get_text())


    def is_title_character(self, input):
        if len(input) != 1:
            return False
        return (
            input.isalpha() or
            input.isdigit() or
            input in [' ', '-', '_', '.']
        )

    def change_write_cursor_pos(self, velocity):
        if 0 <= (self.component.input_bar.get_pos() + velocity) <= len(self.component.input_bar.get_text()):
            self.component.input_bar.change_pos(velocity)
            self.component.input_bar.set_display(self.component.input_bar.get_text())



    