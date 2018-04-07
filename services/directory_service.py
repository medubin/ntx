
from pathlib import Path
import os
from base.base_service import BaseService

class DirectoryService(BaseService):
    def scroll(self, direction):
        if 0 <= (self.component.navigation.get_file_index() + direction) <= len(self.component.navigation.get_files()) - 1:
            self.component.navigation.change_file_index(direction)
            self.component.navigation.set_focus(self.component.navigation.get_file_index())
            
    
    def all_files(self):
        files = []
        # get all files
        for dirpath,_,filenames in os.walk(self.component.navigation.BASE_DIRECTORY):
            for f in filenames:
                files.append(os.path.abspath(os.path.join(dirpath, f)))
        
        return files





