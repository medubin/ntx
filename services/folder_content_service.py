import os
from base.base_service import BaseService
class FolderContentService(BaseService):
    def view(self, folder):

        self.store.opened_file = '\n'.join(os.listdir(folder))
        self.component.open_file.widget.set_text(self.store.opened_file)

    def open(self, folder):
        self.store.push_directory(folder)
        self.store.selected_file = 0
        self.service.state.set_to_browse()

    def close(self):
        if len(self.store.directory) > 0:
            self.store.pop_directory()
            self.store.selected_file = 0
            self.service.state.set_to_browse()

        