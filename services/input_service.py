from base.base_service import BaseService

class InputService(BaseService):
    def push(self, input):
        self.component.input_bar.push_text(input)
        self.component.input_bar.set_display(self.component.input_bar.get_text())
    
    def pop(self):
        self.component.input_bar.pop_text()
        self.component.input_bar.set_display(self.component.input_bar.get_text())