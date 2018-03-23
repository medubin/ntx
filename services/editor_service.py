import sys, tempfile, os
from subprocess import call
from services.base_service import BaseService

class EditorService(BaseService):
    def __init__(self, env):
        self.env = env
   
    def edit_file(self, file):
        self.__open_editor(file)
        self.service.state.set_to_browse()
        

    def __open_editor(self, file):
        EDITOR = os.environ.get('EDITOR') if os.environ.get('EDITOR') else 'vim'
        with self.service.file_content.open(file) as f:
            f.flush()
            call([EDITOR, f.name])
            f.seek(0) # test if this is necessary
            f.read() # test if this is necessary










