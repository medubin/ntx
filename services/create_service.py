import os
from base.base_service import BaseService
from constants.state import State

class CreateService(BaseService):        
    def base_folder(self):
        if not os.path.isdir(self.store.BASE_DIRECTORY):
            os.makedirs(self.store.BASE_DIRECTORY)

    def note(self, filepath):
        file = self.service.file_content.open(filepath + '.md',"a") 
        file.close() 
        self.service.state.set_to_browse()
    
    def folder(self, folderpath):
        if not os.path.isdir(folderpath):
            os.makedirs(folderpath)
        self.service.state.set_to_browse()

    def folder_or_note(self, full_path):
        if self.store.state == State.NEW_FILE: 
            self.service.create.note(full_path)
        elif self.store.state == State.NEW_FOLDER:
            self.service.create.folder(full_path)