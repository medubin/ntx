import os
from pathlib import Path
from services.base_service import BaseService

class DirectoryService(BaseService):
    def __init__(self, env):
        self.env = env

    def view_file_or_folder(self):
        file = self.store.selected_file_name()
        full_path = self.store.full_directory() + '/' + file
        if not os.path.isdir(full_path):
            self.service.file_content.view()
        else:
            self.view_folder_contents()

    def open_folder_or_file(self):
        file = self.store.selected_file_name()
        full_path = self.store.full_directory() + '/' + file
        if not os.path.isdir(full_path):
            self.service.editor.edit_file(file)
        else:
            self.open_folder(file)
        
    def open_folder(self, folder):
        self.store.push_directory(folder)
        self.store.selected_file = 0
        self.service.state.set_to_browse()
    
    def leave_folder(self):
        if len(self.store.directory) > 0:
            self.store.pop_directory()
            self.store.selected_file = 0
            self.service.state.set_to_browse()

    def view_folder_contents(self):
        self.store.opened_file = '\n'.join(os.listdir(self.store.full_directory() + '/' + self.store.selected_file_name()))
        self.component.open_file.widget.set_text(self.store.opened_file)



