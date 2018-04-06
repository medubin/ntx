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
        self.__write_cursor_pos = 0 #distance from the end

        self.opened_file = '' #opened file contents
        self.state = State.BROWSE 

        self.__tags = {}
        self.__selected_tag = ''

        
        
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

    def insert_write_buffer(self, char, pos):
        self.__write_buffer = self.__write_buffer[:pos] + char + self.__write_buffer[pos:]

    def splice_write_buffer(self, pos):
        if(pos == 0):
            return
            
        self.__write_buffer = self.__write_buffer[:pos - 1] + self.__write_buffer[pos:]



    #write cursor pos
    def get_write_cursor_pos(self):
        return self.__write_cursor_pos
    
    def set_write_cursor_pos(self, pos):
        self.__write_cursor_pos = pos
    
    def change_write_cursor_pos(self, velocity):
        self.__write_cursor_pos += velocity

    
    # tags
    def get_tags(self):
        return self.__tags

    def set_tags(self, tags):
        self.__tags = tags

    #selected tag
    def get_selected_tag(self):
        return self.__selected_tag

    def set_selected_tag(self, tag):
        self.__selected_tag = tag


