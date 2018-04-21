from ntx.env import Env

class Browser:
    def __init__(self):
        self.env = Env()
        
    def startup(self):
        self.env.service.create.base_folder()

    def run(self):
        full_path = self.env.component.navigation.get_full_directory() + '/' + self.env.component.navigation.get_selected_file_name() 
        self.env.service.content.view(full_path)
        self.env.component.run()
        
        # print(full_path)
        
    
    def exit(self):
        print('exiting. goodbye.')

    def __input_filter(self, input, raw):
        return input
