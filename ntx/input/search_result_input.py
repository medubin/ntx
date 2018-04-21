from ntx.constants.state import State
from ntx.base.base_input import BaseInput
class SearchResultInput(BaseInput):
    def listen(self, input, state):
        if state != State.SEARCH_RESULT:
            return

        if input == 'up':
            self.component.navigation.scroll(-1)
            full_path = self.component.navigation.BASE_DIRECTORY + '/' + self.component.navigation.get_selected_file_name()
            self.service.content.view(full_path)
        elif input == 'down':
            self.component.navigation.scroll(1)
            full_path = self.component.navigation.BASE_DIRECTORY + '/' + self.component.navigation.get_selected_file_name()
            self.service.content.view(full_path)
        elif input == 'enter' or input == 'right':
            file = self.component.navigation.get_selected_file_name()
            full_path = self.component.navigation.BASE_DIRECTORY + '/' + file
            self.service.editor.edit_file(full_path)
        elif input == 'esc':
            self.component.navigation.pop_file_index()
            self.service.state.browse()
        
  
