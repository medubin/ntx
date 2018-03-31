import os
from base.base_service import BaseService
from constants.state import State
class StateService(BaseService):
    def browse(self):
        self.store.state = State.BROWSE 
        self.store.set_write_buffer('')
        self.store.input_state = ''
        self.store.set_files(self.store.get_full_directory())
        self.component.input_bar.set_text('')
        self.component.files.content[:] = self.component.files.create_files(self.store.get_files())
        self.component.files.set_focus(self.store.get_file_index())
        self.service.content.view()

    def new_note(self):
        self.store.state = State.NEW_FILE
        self.store.input_state = 'new note: '
        self.component.input_bar.set_text('')
        
    def new_folder(self):
        self.store.state = State.NEW_FOLDER
        self.store.input_state = 'new folder: '
        self.component.input_bar.set_text('')

    def search(self):
        self.store.state = State.SEARCH_INPUT
        self.store.input_state = 'search: '
        self.component.input_bar.set_text('')

    def search_results(self):
        self.store.state = State.SEARCH_RESULT
        self.store.push_file_index(0)
        self.store.set_write_buffer('')
        self.store.input_state = ''
        self.component.input_bar.set_text('')
        self.component.files.content[:] = self.component.files.create_files(self.store.search_results)
        self.component.files.set_focus(0)

    def delete(self):
        self.store.state = State.DELETE
        self.store.input_state = 'delete? (Y/n) '
        self.component.input_bar.set_text('')
    
    def command(self):
        self.store.state = State.COMMAND
        self.store.input_state = 'Command:'
        self.component.input_bar.set_text('')



    
