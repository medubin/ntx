from base.base_service import BaseService

class InputService(BaseService):
    def push(self, input):
        self.component.input.push_text(input)
        self.component.input.set_display(self.component.input.get_text())
    
    def pop(self):
        self.component.input.pop_text()
        self.component.input.set_display(self.component.input.get_text())