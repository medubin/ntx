from services.base_service import BaseService
import os
from collections import deque
class SearchService(BaseService):
    def __init__(self, env):
        self.env = env

    def search(self, search_string):
        matches = self.search_files(search_string)
        self.store.search_results = matches

    
    def search_files(self, search_string):
        files = []
        # get all files
        for dirpath,_,filenames in os.walk(self.store.BASE_DIRECTORY):
            for f in filenames:
                files.append(os.path.abspath(os.path.join(dirpath, f)))
            
        matches = []
        for file in files:
            with open(file, 'r') as f:
                content = f.read()
                if search_string in content:
                    matches.append(file)
        
        return matches
    
    # def open_search_result(self, file):
        