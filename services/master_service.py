from services.directory_service import DirectoryService
from services.markdown_service import MarkdownService

class MasterService:
    def __init__(self, store, term):
        self.store = store
        self.term = term

        self.directory_service = DirectoryService(store, term, self)
        self.markdown_service = MarkdownService(store, term, self)