from services.directory_service import DirectoryService
from services.markdown_service import MarkdownService
from services.editor_service import EditorService

class MasterService:
    def __init__(self, store):
        self.store = store

        self.directory_service = DirectoryService(store, self)
        self.markdown_service = MarkdownService(store, self)
        self.editor_service = EditorService(store, self)