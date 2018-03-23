import os
from services.base_service import BaseService
class StateService(BaseService):
    def __init__(self, env):
        self.env = env

    def set_to_browse(self):
        self.store.write_buffer = ''
        self.store.input_state = ''
        self.store.files = os.listdir(self.store.full_directory())
        self.store.state = self.store.STATE_BROWSE 
        self.component.input_bar.set_text('')
        self.component.files.content[:] = self.component.files.create_files(self.store.files)
        self.component.files.set_focus(0)
        

    def new_note(self):
        self.store.state = self.store.STATE_NEW_FILE
        self.store.input_state = 'new note: '
        self.component.input_bar.set_text('')
        
    def new_folder(self):
        self.store.state = self.store.STATE_NEW_FOLDER
        self.store.input_state = 'new folder: '
        self.component.input_bar.set_text('')

    def search(self):
        self.store.state = self.store.STATE_SEARCH_INPUT
        self.store.input_state = 'search: '
        self.component.input_bar.set_text('')

    def search_results(self):
        self.store.state = self.store.STATE_SEARCH_RESULT
        self.store.selected_file = 0
        self.store.write_buffer = ''
        self.store.input_state = ''
        self.component.input_bar.set_text('')
        self.component.files.content[:] = self.component.files.create_files(self.store.search_results)
        self.component.files.set_focus(0)




    
