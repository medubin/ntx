from pathlib import Path
import os

class MasterStore:
    STATE_BROWSE = "BROWSE"
    STATE_NEW_FILE = "NEW_FILE"
    STATE_NEW_FOLDER = "NEW_FOLDER"
    STATE_SEARCH_INPUT = "SEARCH_INPUT"
    STATE_SEARCH_RESULT = "SEARCH_RESULT"
    BASE_DIRECTORY = str(Path.home()) + '/.ntx'

    def __init__(self):
        self.opened_file = '' #opened file contents
        self.state = self.STATE_BROWSE 
        self.write_buffer = ''
        self.selected_file = 0 #selected file index
        self.files = os.listdir(self.BASE_DIRECTORY)
        self.directory = ''
        self.input_state = ''
        self.search_results = []
        
    def push_directory(self, new_directory):
        self.directory += '/' + new_directory
    
    def pop_directory(self):
        self.directory = '/'.join(self.directory.split('/')[:-1])

    def selected_file_name(self):
        return self.files[self.selected_file]
    
    def full_directory(self):
        return self.BASE_DIRECTORY + self.directory


