import os
import shutil
from base.base_service import BaseService

class DeleteService(BaseService):        
    def note(self, filepath):
        os.remove(filepath) 

    def folder(self, folderpath):
       shutil.rmtree(folderpath)

    def folder_or_note(self, full_path):
        self.store.change_file_index(-1)
        if os.path.isdir(full_path):
            self.folder(full_path)
        else:
            self.note(full_path)
