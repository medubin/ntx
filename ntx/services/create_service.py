import os
from ntx.base.base_service import BaseService
from ntx.constants.state import State
import ntx.helpers.file_content_helper as file_content

class CreateService(BaseService):        
    def base_folder(self):
        if not os.path.isdir(self.component.navigation.BASE_DIRECTORY):
            os.makedirs(self.component.navigation.BASE_DIRECTORY)

    def note(self, filepath):
        file = file_content.open_note(filepath + '.md',"a") 
        file.close() 
        self.service.state.browse()
    
    def folder(self, folderpath):
        if not os.path.isdir(folderpath):
            os.makedirs(folderpath)
        self.service.state.browse()