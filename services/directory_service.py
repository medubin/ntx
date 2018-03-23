import os
from pathlib import Path

class DirectoryService:
    

    def __init__(self, env):
        self.env = env
        self.env.store.files = os.listdir(self.env.store.BASE_DIRECTORY)

    def view_file_or_folder(self):
        file = self.env.store.selected_file_name()
        full_path = self.env.store.full_directory() + '/' + file
        if not os.path.isdir(full_path):
            self.env.service.file_content.view()
        else:
            self.view_folder_contents()

    def open_folder_or_file(self):
        file = self.env.store.selected_file_name()
        full_path = self.env.store.full_directory() + '/' + file
        if not os.path.isdir(full_path):
            self.env.service.editor.edit_file(file)
        else:
            self.open_folder(file)
        

    def open_folder(self, folder):
        self.env.store.push_directory(folder)
        self.env.store.selected_file = 0
        self.env.service.state.set_to_browse()
    
    def leave_folder(self):
        if len(self.env.store.directory) > 0:
            self.env.store.pop_directory()
            self.env.store.selected_file = 0
            self.env.service.state.set_to_browse()

    def view_folder_contents(self):
        self.env.store.opened_file = '\n'.join(os.listdir(self.env.store.full_directory() + '/' + self.env.store.selected_file_name()))
        self.env.component.open_file.widget.set_text(self.env.store.opened_file)



