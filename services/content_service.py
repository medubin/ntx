import os
from base.base_service import BaseService
class ContentService(BaseService):
    
    def open(self):
        file = self.store.selected_file_name()
        if not file:
            return

        full_path = self.store.get_full_directory() + '/' + file
        if not os.path.isdir(full_path):
            self.service.editor.edit_file(full_path)
        else:
            self.service.folder_content.open(file)

    def view(self):
        file = self.store.selected_file_name()
        if not file:
            return

        full_path = self.store.get_full_directory() + '/' + file
        if not os.path.isdir(full_path):
            self.service.file_content.view()
        else:
            self.service.folder_content.view(full_path)
        
        