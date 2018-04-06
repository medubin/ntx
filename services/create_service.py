import os
from base.base_service import BaseService
from constants.state import State
import helpers.file_content_helper as file_content

class CreateService(BaseService):        
    def base_folder(self):
        if not os.path.isdir(self.store.BASE_DIRECTORY):
            os.makedirs(self.store.BASE_DIRECTORY)

    def note(self, filepath):
        file = file_content.open_note(filepath + '.md',"a") 
        file.close() 
        self.service.state.browse()
    
    def folder(self, folderpath):
        if not os.path.isdir(folderpath):
            os.makedirs(folderpath)
        self.service.state.browse()

    def folder_or_note(self, full_path):
        if self.store.state == State.NEW_FILE: 
            self.note(full_path)
        elif self.store.state == State.NEW_FOLDER:
            self.folder(full_path)
