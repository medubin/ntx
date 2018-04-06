import sys, tempfile, os
from subprocess import call

import helpers.file_content_helper as file_content

from base.base_service import BaseService

class EditorService(BaseService):
    def edit_file(self, filepath):
        self.__open_editor(filepath)
        self.service.state.browse()
        

    def __open_editor(self, filepath):
        EDITOR = os.environ.get('EDITOR') if os.environ.get('EDITOR') else 'vim'
        with file_content.open_note(filepath) as f:
            f.flush()
            call([EDITOR, f.name])
            f.seek(0) # test if this is necessary
            f.read() # test if this is necessary
        self.component.loop.stop()
        self.component.run()
