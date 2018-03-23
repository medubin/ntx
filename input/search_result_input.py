from constants.state import State
class SearchResultInput:
    def __init__(self, env):
        self.env = env

    def listen(self, input, state):
        if state != State.SEARCH_RESULT:
            return

        if input == 'up':
            self.env.service.directory.scroll_up()
            self.env.service.directory.view_file_or_folder()
        elif input == 'down':
            self.env.service.directory.scroll_down()
            self.env.service.directory.view_file_or_folder()
        elif input == 'enter' or input == 'right':
            file = self.env.store.search_results[self.env.store.selected_file]
            self.env.service.editor.edit_file(file)
  
