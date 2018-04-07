import os
from base.base_service import BaseService
class ContentService(BaseService):
    
    def open(self):
        file = self.component.navigation.get_selected_file_name()
        if not file:
            return

        full_path = self.component.navigation.get_full_directory() + '/' + file
        if not os.path.isdir(full_path):
            self.service.editor.edit_file(full_path)
        else:
            self.service.folder_content.open(file)

    def view(self, full_path):
        if not os.path.isdir(full_path):
            self.service.file_content.view(full_path)
        else:
            self.service.folder_content.view(full_path)
        
        