import os
from base.base_service import BaseService
class FolderContentService(BaseService):
    def view(self, folder):

        self.store.opened_file = '\n'.join(os.listdir(folder))
        self.component.open_file.widget.set_text(self.store.opened_file)

    def open(self, folder):
        self.store.push_directory(folder)
        self.store.push_file_index(0)
        self.service.state.browse()

    def close(self):
        if len(self.store.get_directory()) > 0:
            self.store.pop_directory()
            self.store.pop_file_index()
            self.service.state.browse()

        