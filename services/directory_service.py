import pager
import os
from pathlib import Path

class DirectoryService:
    base_directory = str(Path.home()) + '/.ntx'
    def __init__(self, store, term, service):
        self.store = store
        self.term = term
        self.service = service
        self.store.files = os.listdir(self.base_directory)
    
    def create_base_directory(self):
        if not os.path.isdir(self.base_directory):
            os.makedirs(self.base_directory)
    
    def create_new_note(self):
        file = open(self.base_directory + '/' + self.store.write_buffer + ".md","w") 
        file.close() 
        self.store.write_buffer = ''
        self.store.files = os.listdir(self.base_directory)
        self.store.state = self.store.STATE_BROWSE
    
    def get_selected_file(self):
        if self.store.selected_file == -1:
            return None
        
        return self.store.files[self.store.selected_file]

    def get_file_contents(self, file):
        with open(self.base_directory + '/' + file) as f:
            return f.read()





    




    
