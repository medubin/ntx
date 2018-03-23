
from services.base_service import BaseService
class FileContentService(BaseService):
    def __init__(self, env):
        self.env = env

    def get(self, file):
        with self.open(file) as f:
            return self.service.markdown.parse(f.read())
    
    def open(self, file, type ='r'):
        return open(self.store.full_directory() + '/' + file, type)

    def view(self):
        file = self.store.selected_file_name()
        if (file is not None):
            self.store.opened_file = self.service.file_content.get(file)
            self.component.open_file.widget.set_text(self.store.opened_file)



        