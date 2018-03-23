import sys, tempfile, os
from subprocess import call
from base.base_service import BaseService

class EditorService(BaseService):
    def edit_file(self, filepath):
        self.__open_editor(filepath)
        self.service.state.set_to_browse()
        

    def __open_editor(self, filepath):
        EDITOR = os.environ.get('EDITOR') if os.environ.get('EDITOR') else 'vim'
        with self.service.file_content.open(filepath) as f:
            f.flush()
            call([EDITOR, f.name])
            f.seek(0) # test if this is necessary
            f.read() # test if this is necessary










