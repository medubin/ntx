from pathlib import Path
import os
from constants.state import State

class MasterStore:
    BASE_DIRECTORY = str(Path.home()) + '/.ntx'

    def __init__(self):
        self.opened_file = '' #opened file contents
        self.state = State.BROWSE 
        self.write_buffer = ''
        self.__file_indices = [0] #selected file index
        self.files = os.listdir(self.BASE_DIRECTORY)
        self.directory = ''
        self.input_state = ''
        self.search_results = []
        
    def push_directory(self, new_directory):
        self.directory += '/' + new_directory
    
    def pop_directory(self):
        self.directory = '/'.join(self.directory.split('/')[:-1])

    def selected_file_name(self):
        return self.files[self.get_file_index()]
    
    def full_directory(self):
        return self.BASE_DIRECTORY + self.directory


    #file index
    def get_file_index(self):
        return self.__file_indices[-1]
    
    def pop_file_index(self):
        self.__file_indices = self.__file_indices[:-1]

    def push_file_index(self, index):
        self.__file_indices.append(index)
    
    def change_file_index(self, velocity):
        self.__file_indices[-1] += velocity




