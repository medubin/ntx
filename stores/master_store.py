import os
from constants.state import State

class MasterStore:
    

    def __init__(self):
        self.__file_indices = [0]
        self.__files = []
        self.__directory = ''

        self.state = State.BROWSE 

        self.__tags = {}
        self.__selected_tag = ''

        
        
        self.input_state = ''
        self.search_results = []

        
        

    
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


