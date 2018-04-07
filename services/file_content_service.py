import helpers.markdown_helper as markdown
import helpers.file_content_helper as file_content_helper
from base.base_service import BaseService
class FileContentService(BaseService):
    def view(self, full_path):
        self.component.display.set_text(file_content_helper.get(full_path))
        self.component.display.set_display()




