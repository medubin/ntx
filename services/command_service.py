
from base.base_service import BaseService
from constants.command import Command
import os
class CommandService(BaseService):
    def interpret(self, command):
        parsed = command.split(' ')
        command_name = parsed[0]
        if len(parsed) > 1:
            command_target = parsed[1]
        else:
            command_target = ''

        if command_name == Command.NEW_NOTE:
            full_path = self.store.get_full_directory() + '/' + command_target
            self.service.create.note(full_path)
        elif command_name == Command.NEW_FOLDER:
            full_path = self.store.get_full_directory() + '/' + command_target
            self.service.create.folder(full_path)
        elif command_name == Command.DELETE:
            full_path = self.store.get_full_directory() + '/' + self.store.selected_file_name()
            self.service.delete.folder_or_note(full_path)
            self.service.state.browse()
        elif command_name == Command.SEARCH:
            self.service.search.search(command_target)
            self.service.state.search_results()
        elif command_name == Command.TAGS:
            self.service.tag.get()
            self.service.state.tags()



    def autocomplete(self, input):
        possible_commands = list(filter(lambda x: x.startswith(input), Command.ALL))

        if len(possible_commands) > 0:
             self.component.input_bar.set_text(os.path.commonprefix(possible_commands))
             self.component.input_bar.set_display(self.component.input_bar.get_text())
