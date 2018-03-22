import os
class StateService:
    def __init__(self, env):
        self.env = env

    def set_to_browse(self):
        self.env.store.write_buffer = ''
        self.env.store.files = os.listdir(self.env.service.directory.base_directory + self.env.store.directory)
        self.env.store.state = self.env.store.STATE_BROWSE 


    
