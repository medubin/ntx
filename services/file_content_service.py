import helpers.markdown_helper as markdown
import helpers.file_content_helper as file_content
from base.base_service import BaseService
class FileContentService(BaseService):
    # def get(self, file):
    #     with self.open(file) as f:
    #         return markdown.parse(f.read())
    
    # def open(self, file, type ='r'):
    #     return open(file, type)

    def view(self, full_path):
        self.store.opened_file = file_content.get(full_path)
        self.component.open_file.widget.set_text(self.store.opened_file)



