import ntx.helpers.file_content_helper as file_content_helper
from ntx.base.base_service import BaseService
class FileContentService(BaseService):
    def view(self, full_path):
        self.component.display.set_text(self.get(full_path))

    def get(self, file):
        with file_content_helper.open_note(file) as f:
            return self.service.markdown.parse(f.read())




