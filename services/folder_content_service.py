import os
from base.base_service import BaseService
class FolderContentService(BaseService):
    def view(self, folder):
        self.component.display.set_text('\n'.join(os.listdir(folder)))
        self.component.display.set_display()

    def open(self, folder):
        self.store.push_directory(folder)
        self.component.navigation.push_file_index(0)
        self.service.state.browse()

    def close(self):
        if len(self.store.get_directory()) > 0:
            self.store.pop_directory()
            self.component.navigation.pop_file_index()
            self.service.state.browse()

        