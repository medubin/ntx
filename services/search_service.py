from base.base_service import BaseService
import os

import helpers.search_helper as search

class SearchService(BaseService):
    def search(self, search_string):
        files = self.service.directory.all_files()
        base_directory = self.store.BASE_DIRECTORY
        
        matches = search.search_files(search_string, files, base_directory)
        self.store.search_results = matches

    

        