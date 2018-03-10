import sys, tempfile, os
from subprocess import call

class EditorService:
    def __init__(self, store, term, service):
        self.store = store
        self.term = term
        self.service = service

    def open_selected_file(self):
        file = self.service.directory_service.get_selected_file()
        if (file is not None):
            self.open_editor(file)
        
    def open_editor(self, file):
        EDITOR = os.environ.get('EDITOR') if os.environ.get('EDITOR') else 'vim'
        with self.service.directory_service.open_file(file) as f:
            f.flush()
            call([EDITOR, f.name])
            f.seek(0) # test if this is necessary
            f.read() # test if this is necessary










