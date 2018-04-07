import os
from base.base_service import BaseService
from constants.state import State
class StateService(BaseService):
    def browse(self):
        self.store.state = State.BROWSE 
        self.component.input_bar.set_text('')
        self.store.input_state = ''
        self.component.navigation.set_files_from_directory(self.component.navigation.get_full_directory())
        self.component.input_bar.set_display('')
        self.component.navigation.content[:] = self.component.navigation.create_files(self.component.navigation.get_files())
        self.component.navigation.set_focus(self.component.navigation.get_file_index())

    def search_results(self):
        self.store.state = State.SEARCH_RESULT
        self.component.navigation.push_file_index(0)
        self.component.input_bar.set_text('')
        self.store.input_state = ''
        self.component.input_bar.set_display('')
        self.component.navigation.content[:] = self.component.navigation.create_files(self.component.navigation.get_files())
        self.component.navigation.set_focus(0)

    def tags(self):
        self.store.state = State.TAGS
        self.component.navigation.push_file_index(0)
        self.component.input_bar.set_text('')
        self.store.input_state = ''
        self.component.input_bar.set_display('')
        self.component.navigation.set_files(list(self.component.navigation.get_tags().keys()))
        self.component.navigation.content[:] = self.component.navigation.create_files(self.component.navigation.get_files())
        self.component.navigation.set_focus(0)

    def command(self):
        self.store.state = State.COMMAND
        self.store.input_state = 'Command:'
        self.component.input_bar.set_display('')

