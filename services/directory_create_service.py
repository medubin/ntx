import os
from services.base_service import BaseService

class DirectoryCreateService(BaseService):
    def __init__(self, env):
        self.env = env
        
    def base_folder(self):
        if not os.path.isdir(self.store.BASE_DIRECTORY):
            os.makedirs(self.store.BASE_DIRECTORY)

    def note(self):
        file = self.service.file_content.open(self.store.write_buffer + ".md","a") 
        file.close() 
        self.service.state.set_to_browse()
    
    def folder(self, directory = None):
        if not directory:
            directory = self.store.full_directory() + '/' + self.store.write_buffer
        if not os.path.isdir(directory):
            os.makedirs(directory)
        self.service.state.set_to_browse()