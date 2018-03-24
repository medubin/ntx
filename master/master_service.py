from services.directory_service import DirectoryService
from services.create_service import CreateService
from services.editor_service import EditorService
from services.file_content_service import FileContentService
from services.search_service import SearchService
from services.markdown_service import MarkdownService
from services.state_service import StateService
from services.input_service import InputService
from services.folder_content_service import FolderContentService
from services.content_service import ContentService
from services.delete_service import DeleteService

class MasterService:
    def __init__(self, env):
        self.env = env

        self.content = ContentService(env)
        self.create = CreateService(env)
        self.delete = DeleteService(env)
        self.directory = DirectoryService(env)
        self.editor = EditorService(env)
        self.file_content = FileContentService(env)
        self.folder_content = FolderContentService(env)
        self.input = InputService(env)
        self.markdown = MarkdownService(env)
        self.state = StateService(env)
        self.search = SearchService(env)
        
    def setup(self):
        self.create.setup()
        self.content.setup()
        self.delete.setup()
        self.directory.setup()
        self.editor.setup()
        self.file_content.setup()
        self.folder_content.setup()
        self.input.setup()
        self.markdown.setup()
        self.state.setup()
        self.search.setup()
        
        
