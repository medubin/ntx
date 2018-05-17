
from ntx.base.base_service import BaseService
from ntx.constants.command import Command
import os
import sys
class CommandService(BaseService):
    def interpret(self, command):
        parsed = command.split(' ')
        command_name = parsed[0]
        if len(parsed) > 1:
            command_target = ' '.join(parsed[1:])
        else:
            command_target = ''

        if command_name == Command.NEW_NOTE:
            full_path = self.component.navigation.get_full_directory() + '/' + command_target
            self.service.create.note(full_path)
        elif command_name == Command.NEW_FOLDER:
            full_path = self.component.navigation.get_full_directory() + '/' + command_target
            self.service.create.folder(full_path)
        elif command_name == Command.DELETE:
            full_path = self.component.navigation.get_full_directory() + '/' + self.component.navigation.get_selected_file_name()
            self.service.delete.folder_or_note(full_path)
            self.service.state.browse()
        elif command_name == Command.SEARCH:
            if self.service.search.search(command_target):
                self.service.state.search_results()
                full_path = self.component.navigation.BASE_DIRECTORY + '/' + self.component.navigation.get_selected_file_name()
                self.service.content.view(full_path)
            else: 
                self.service.state.browse()
        elif command_name == Command.TAGS:
            self.service.tag.get()
            self.service.state.tags()
            self.service.tag.view()
        elif command_name == Command.EXIT:
            sys.exit()


    def autocomplete(self, input):
        possible_commands = list(filter(lambda x: x.startswith(input), Command.ALL))

        if len(possible_commands) > 0:
             self.component.input.set_text(os.path.commonprefix(possible_commands))
             self.component.input.set_display(self.component.input.get_text())
