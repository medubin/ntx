
from services.base_service import BaseService
class FileContentService(BaseService):
    def __init__(self, env):
        self.env = env

    def get(self, file):
        with self.open(file) as f:
            return self.service.markdown.parse(f.read())
    
    def open(self, file, type ='r'):
        return open(file, type)

    def view(self):
        file = self.store.selected_file_name()
        filepath = self.store.full_directory() + '/' + file
        if (file is not None):
            self.store.opened_file = self.get(filepath)
            self.component.open_file.widget.set_text(self.store.opened_file)



        