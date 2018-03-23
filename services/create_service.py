import os
from services.base_service import BaseService

class CreateService(BaseService):
    def __init__(self, env):
        self.env = env
        
    def base_folder(self):
        if not os.path.isdir(self.store.BASE_DIRECTORY):
            os.makedirs(self.store.BASE_DIRECTORY)

    def note(self, filepath):
        file = self.service.file_content.open(filepath,"a") 
        file.close() 
        self.service.state.set_to_browse()
    
    def folder(self, folderpath):
        if not os.path.isdir(folderpath):
            os.makedirs(folderpath)
        self.service.state.set_to_browse()