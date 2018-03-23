
from pathlib import Path
from base.base_service import BaseService

class DirectoryService(BaseService):
    def scroll(self, direction):
        if 0 <= (self.store.selected_file + direction) <= len(self.store.files) - 1:
            self.store.selected_file += direction 
            self.component.files.widget.focus_position = self.store.selected_file
        self.service.content.view()




