from ntx.services.directory_service import DirectoryService
from ntx.services.create_service import CreateService
from ntx.services.editor_service import EditorService
from ntx.services.file_content_service import FileContentService
from ntx.services.search_service import SearchService
from ntx.services.markdown_parser import MarkdownParser
from ntx.services.state_service import StateService
from ntx.services.input_service import InputService
from ntx.services.folder_content_service import FolderContentService
from ntx.services.content_service import ContentService
from ntx.services.delete_service import DeleteService
from ntx.services.command_service import CommandService
from ntx.services.tag_service import TagService

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
        self.state = StateService(env)
        self.search = SearchService(env)
        self.command = CommandService(env)
        self.tag = TagService(env)

        self.markdown = MarkdownParser()
        
    def setup(self):
        self.create.setup()
        self.content.setup()
        self.delete.setup()
        self.directory.setup()
        self.editor.setup()
        self.file_content.setup()
        self.folder_content.setup()
        self.input.setup()
        self.state.setup()
        self.search.setup()
        self.command.setup()
        self.tag.setup()
        
        
