
from pathlib import Path
import os
import ntx.helpers.directory_helper as directory_helper
from ntx.base.base_service import BaseService

class DirectoryService(BaseService):
    def all_files(self):
        files = []
        # get all files
        for dirpath,_,filenames in os.walk(self.component.navigation.BASE_DIRECTORY):
            for f in directory_helper.filter_hidden(filenames):
                files.append(os.path.abspath(os.path.join(dirpath, f)))
        
        return files
