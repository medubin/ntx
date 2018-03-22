import sys, tempfile, os
from subprocess import call

class EditorService:
    def __init__(self, env):
        self.env = env
   
    def edit_file(self):
        file = self.env.service.directory.get_selected_file()
        full_path = self.env.service.directory.base_directory + '/' + file
        if not os.path.isdir(full_path):
            self.__open_editor(file)

        
    def __open_editor(self, file):
        EDITOR = os.environ.get('EDITOR') if os.environ.get('EDITOR') else 'vim'
        with self.env.service.file_content.open(file) as f:
            f.flush()
            call([EDITOR, f.name])
            f.seek(0) # test if this is necessary
            f.read() # test if this is necessary










