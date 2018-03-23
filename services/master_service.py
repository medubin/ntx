from services.directory_service import DirectoryService
from services.directory_create_service import DirectoryCreateService
from services.editor_service import EditorService
from services.file_content_service import FileContentService
from services.search_service import SearchService
from services.markdown_service import MarkdownService
from services.state_service import StateService

class MasterService:
    def __init__(self, env):
        self.env = env
        self.directory = DirectoryService(env)
        self.directory_create = DirectoryCreateService(env)
        self.editor = EditorService(env)
        self.file_content = FileContentService(env)
        self.markdown = MarkdownService(env)
        self.state = StateService(env)
        self.search = SearchService(env)
    
    def setup(self):
        self.directory.setup()
        self.directory_create.setup()
        self.editor.setup()
        self.file_content.setup()
        self.markdown.setup()
        self.state.setup()
        self.search.setup()
