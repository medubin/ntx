import os
from pathlib import Path

class DirectoryService:
    base_directory = str(Path.home()) + '/.ntx'

    def __init__(self, env):
        self.env = env
        self.env.store.files = os.listdir(self.base_directory)

    def get_selected_file(self):
        return self.env.store.files[self.env.store.selected_file]

    def view_file_or_folder(self):
        file = self.env.service.directory.get_selected_file()
        full_path = self.env.service.directory.directory() + '/' + file
        if not os.path.isdir(full_path):
            self.env.service.file_content.view()
        else:
            self.open_folder()

    def open_folder(self):
        self.env.store.directory = self.env.store.directory + '/' + self.get_selected_file()
        self.env.store.selected_file = 0
        self.env.service.state.set_to_browse()
    
    def leave_folder(self):
        if len(self.env.store.directory) > 0:
            self.env.store.directory = '/'.join(self.env.store.directory.split('/')[:-1])
            self.env.store.selected_file = 0
            self.env.service.state.set_to_browse()

    def directory(self):
        return self.base_directory + self.env.store.directory



