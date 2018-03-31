from pathlib import Path
import os
from constants.state import State

class MasterStore:
    BASE_DIRECTORY = str(Path.home()) + '/.ntx'

    def __init__(self):
        self.__file_indices = [0]
        self.__files = []
        self.__directory = ''
        self.__write_buffer = ''

        self.opened_file = '' #opened file contents
        self.state = State.BROWSE 
        
        
        self.input_state = ''
        self.search_results = []

        self.set_files(self.BASE_DIRECTORY)
        
    # directory
    def get_directory(self):
        return self.__directory    

    def get_full_directory(self):
        return self.BASE_DIRECTORY + self.__directory
    
    def push_directory(self, new_directory):
        self.__directory += '/' + new_directory
    
    def pop_directory(self):
        self.__directory = '/'.join(self.__directory.split('/')[:-1])

    # files
    def get_files(self):
        return self.__files
    
    def set_files(self, directory):
        folders = []
        notes = []

        all_files = os.listdir(directory)


        for file in all_files:
            full_path = self.get_full_directory() + '/' + file
            if os.path.isdir(full_path):
                folders.append(file)
            else:
                notes.append(file)
            
        self.__files = sorted(folders) + sorted(notes)

    def selected_file_name(self):
        if self.get_file_index() < len(self.__files): 
            return self.__files[self.get_file_index()]
        return None



    #file index
    def get_file_index(self):
        return self.__file_indices[-1]
    
    def pop_file_index(self):
        self.__file_indices = self.__file_indices[:-1]

    def push_file_index(self, index):
        self.__file_indices.append(index)
    
    def change_file_index(self, velocity):
        self.__file_indices[-1] += velocity



    #write buffer
    def get_write_buffer(self):
        return self.__write_buffer
    
    def set_write_buffer(self, write_buffer):
        self.__write_buffer = write_buffer
    
    def push_write_buffer(self, char):
        self.__write_buffer += char
    
    def pop_write_buffer(self):
        self.__write_buffer = self.__write_buffer[:-1]




