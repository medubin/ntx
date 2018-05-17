from ntx.base.base_service import BaseService

class InputService(BaseService):
    def push(self, input):
        self.component.input.push_text(input)
        self.component.input.update_display()
    
    def pop(self):
        self.component.input.pop_text()
        self.component.input.update_display()