import os
from ntx.base.base_service import BaseService
from ntx.constants.state import State
from ntx.constants.messsage import Message
class StateService(BaseService):
    def browse(self):
        self.component.set_state(State.BROWSE)
        self.component.input.reset()
        self.component.navigation.set_files_from_directory(self.component.navigation.get_full_directory())
        self.component.navigation.content[:] = self.component.navigation.create_files(self.component.navigation.get_files())
        self.component.navigation.set_focus(self.component.navigation.get_file_index())
        self.component.message.set_text(Message.BASIC)



    def search_results(self):
        self.component.set_state(State.SEARCH_RESULT)
        self.component.navigation.push_file_index(0)
        self.component.input.reset()
        self.component.navigation.content[:] = self.component.navigation.create_files(self.component.navigation.get_files())
        self.component.navigation.set_focus(0)
        self.component.message.set_text(Message.SEARCH(self.component.navigation.get_last_search()))

    def tags(self):
        self.component.set_state(State.TAGS)
        self.component.navigation.push_file_index(0)
        self.component.input.reset()
        self.component.navigation.set_files(list(self.component.navigation.get_tags().keys()))
        self.component.navigation.content[:] = self.component.navigation.create_files(self.component.navigation.get_files())
        self.component.navigation.set_focus(0)

    def command(self):
        self.component.set_state(State.COMMAND)
        self.component.input.reset(prefix='Command:')


