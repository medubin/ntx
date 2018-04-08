import urwid
import os
from pathlib import Path
from base.base_component import BaseComponent

class Navigation(BaseComponent):
    BASE_DIRECTORY = str(Path.home()) + '/.ntx'
    def __init__(self, env):
        self.env = env


        self.__file_indices = [0]
        self.__files = []
        self.__directory = ''
        self.__tags = {}
        self.__selected_tag = ''

        self.set_files_from_directory(self.BASE_DIRECTORY)

        self.content = urwid.SimpleFocusListWalker(self.create_files(self.get_files()))
        self.widget = self.__render()

      
        

    def __render(self):
        listbox = ListBoxOverride(self.content)
        if len(self.content):
            listbox.set_focus(0)
        return listbox

    def create_files(self, files):
        contents = []
        for file in files:
            full_path = self.get_full_directory() + '/' + file
            content = urwid.Text(file)
            if os.path.isdir(full_path):
                contents.append(urwid.AttrMap(content, 'folder', 'reveal focus'))
            else:
                contents.append(urwid.AttrMap(content, None, 'reveal focus'))

        return contents
    
    def set_focus(self, focus):
        if len(self.content):
            self.widget.set_focus(focus)

    def scroll(self, direction):
        if 0 <= (self.get_file_index() + direction) <= len(self.get_files()) - 1:
            self.change_file_index(direction)
            self.set_focus(self.get_file_index())



    # Getters and Setters

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

    def set_files(self, files):
        self.__files = files
    
    def set_files_from_directory(self, directory):
        folders = []
        notes = []

        all_files = os.listdir(directory)


        for file in all_files:
            if file.startswith('.'):
                continue
            full_path = self.get_full_directory() + '/' + file
            if os.path.isdir(full_path):
                folders.append(file)
            else:
                notes.append(file)
            
        self.__files = sorted(folders) + sorted(notes)

    def get_selected_file_name(self):
        if self.get_file_index() < len(self.__files): 
            return self.__files[self.get_file_index()]
        return ''



    #file index
    def get_file_index(self):
        return self.__file_indices[-1]
    
    def pop_file_index(self):
        self.__file_indices = self.__file_indices[:-1]

    def push_file_index(self, index):
        self.__file_indices.append(index)
    
    def change_file_index(self, velocity):
        self.__file_indices[-1] += velocity

      
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



# overrides the keypress which has some weird behavior in urwid.
class ListBoxOverride(urwid.ListBox):
    def keypress(self, size, key):
        return key
        