import os
import ntx.helpers.directory_helper as directory_helper

from ntx.base.base_service import BaseService
class FolderContentService(BaseService):
    def view(self, folder):
        content = directory_helper.get_files_in_folder(folder)
        self.component.display.set_text('\n'.join(content))

    def open(self, folder):
        self.component.navigation.push_directory(folder)
        self.component.navigation.push_file_index(0)
        self.service.state.browse()
        full_path = self.component.navigation.get_full_directory() + '/' + self.component.navigation.get_selected_file_name() 
        self.service.content.view(full_path)

    def close(self):
        if len(self.component.navigation.get_directory()) > 0:
            self.component.navigation.pop_directory()
            self.component.navigation.pop_file_index()
            self.service.state.browse()

        