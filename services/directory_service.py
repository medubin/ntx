
from pathlib import Path
import os
from base.base_service import BaseService

class DirectoryService(BaseService):
    def all_files(self):
        files = []
        # get all files
        for dirpath,_,filenames in os.walk(self.component.navigation.BASE_DIRECTORY):
            for f in filenames:
                files.append(os.path.abspath(os.path.join(dirpath, f)))
        
        return files





