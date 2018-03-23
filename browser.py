from env import Env

class Browser:
    def __init__(self):
        self.env = Env()
        
    def startup(self):
        self.env.service.directory_create.base_folder()

    def run(self):
        self.env.component.run()
    
    def exit(self):
        print('exiting. goodbye.')

    def __input_filter(self, input, raw):
        return input
