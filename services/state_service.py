import os
from services.base_service import BaseService
class StateService(BaseService):
    def __init__(self, env):
        self.env = env

    def set_to_browse(self):
        self.store.write_buffer = ''
        self.store.files = os.listdir(self.store.full_directory())
        self.store.state = self.store.STATE_BROWSE 
        self.component.input_bar.widget.set_text('')
        self.component.files.content[:] = self.component.files.create_files()
        self.component.files.widget.set_focus(0)



    
