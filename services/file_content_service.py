
from base.base_service import BaseService
class FileContentService(BaseService):
    def get(self, file):
        with self.open(file) as f:
            return self.service.markdown.parse(f.read())
    
    def open(self, file, type ='r'):
        return open(file, type)

    def view(self, full_path):
        self.store.opened_file = self.get(full_path)
        self.component.open_file.widget.set_text(self.store.opened_file)



        