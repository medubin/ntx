from constants.state import State
from base.base_input import BaseInput
class TagsInput(BaseInput):
    def listen(self, input, state):
        if state != State.TAGS:
            return

        if input == 'up':
            self.service.directory.scroll(-1)
            self.service.tag.view()
        elif input == 'down':
            self.service.directory.scroll(1)
            self.service.tag.view()
        elif input == 'enter' or input == 'right':
            if (self.store.get_selected_tag()):
                file = self.store.get_tags()[self.store.get_selected_tag()][self.component.navigation.get_file_index()]
                full_path = self.component.navigation.BASE_DIRECTORY + '/' + file
                self.service.editor.edit_file(full_path)
            else:
                tag = list(self.store.get_tags().keys())[self.component.navigation.get_file_index()]
                self.service.tag.open_tag(tag)
        elif input == 'left':
            self.service.tag.leave_tag()
        

                

                        
        elif input == 'esc':
            self.component.navigation.pop_file_index()
            self.service.state.browse()
        
  
