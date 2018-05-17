from ntx.base.base_service import BaseService
from ntx.constants.messsage import Message
import os


import ntx.helpers.search_helper as search

class SearchService(BaseService):
    def search(self, search_string):
        files = self.service.directory.all_files()
        base_directory = self.component.navigation.BASE_DIRECTORY

        matches = search.search_files(search_string, files, base_directory)
        if matches:
            self.component.navigation.set_files(matches)
            return True
        else:
            self.component.message.set_text(Message.SEARCH_FAILED)
            return False
            

    

        