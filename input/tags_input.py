from constants.state import State
from base.base_input import BaseInput
class TagsInput(BaseInput):
    def listen(self, input, state):
        if state != State.TAGS:
            return

        if input == 'up':
            self.service.directory.scroll(-1)
        elif input == 'down':
            self.service.directory.scroll(1)
        elif input == 'enter' or input == 'right':
            if (self.store.get_selected_tag()):
                file = self.store.get_tags()[self.store.get_selected_tag()][self.store.get_file_index()]
                self.service.editor.edit_file(file)
            else:
                tag = self.store.get_tags()[self.store.get_file_index()]
                self.store.set_selected_tag(tag)
                print(tag)
            
        elif input == 'esc':
            self.store.pop_file_index()
            self.service.state.browse()
        
  
