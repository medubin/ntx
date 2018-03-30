
from base.base_service import BaseService
class CommandService(BaseService):
    def interpret(self, command):
        parsed = command.split(' ')
        command_name = parsed[0]
        if len(parsed) > 1:
            command_target = parsed[1]
        else:
            command_target = ''

        if command_name == 'new-note':
            full_path = self.store.get_full_directory() + '/' + command_target
            self.service.create.note(full_path)
        elif command_name == 'new-folder':
            full_path = self.store.get_full_directory() + '/' + command_target
            self.service.create.folder(full_path)
        elif command_name == 'delete':
            full_path = self.store.get_full_directory() + '/' + self.store.selected_file_name()
            self.service.delete.folder_or_note(full_path)
            self.service.state.browse()
        elif command_name == 'search':
            self.service.search.search(command_target)
            self.service.state.search_results()



        

        