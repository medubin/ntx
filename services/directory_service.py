
from pathlib import Path
from base.base_service import BaseService

class DirectoryService(BaseService):
    def scroll(self, direction):
        if 0 <= (self.store.get_file_index() + direction) <= len(self.store.get_files()) - 1:
            self.store.change_file_index(direction)
            self.component.files.widget.focus_position = self.store.get_file_index()
        self.service.content.view()




