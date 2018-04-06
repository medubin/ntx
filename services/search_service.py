from base.base_service import BaseService
import os

class SearchService(BaseService):
    def search(self, search_string):
        matches = self.search_files(search_string)
        self.store.search_results = matches

    
    def search_files(self, search_string):
        files = self.service.directory.all_files()
        
        matches = []
        removal_length = len(self.store.BASE_DIRECTORY) + 1
        for file in files:
            with open(file, 'r') as f:
                content = f.read()
                if search_string in content:
                    matches.append(file[removal_length:])
        
        return matches
    
        