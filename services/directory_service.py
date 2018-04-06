
from pathlib import Path
import os
from base.base_service import BaseService

class DirectoryService(BaseService):
    def scroll(self, direction):
        if 0 <= (self.store.get_file_index() + direction) <= len(self.store.get_files()) - 1:
            self.store.change_file_index(direction)
            self.component.files.widget.focus_position = self.store.get_file_index()
            
    
    def all_files(self):
        files = []
        # get all files
        for dirpath,_,filenames in os.walk(self.store.BASE_DIRECTORY):
            for f in filenames:
                files.append(os.path.abspath(os.path.join(dirpath, f)))
        
        return files





