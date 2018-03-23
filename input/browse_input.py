from constants.state import State

class BrowseInput:
    def __init__(self, env):
        self.env = env

    def listen(self, input, state):
        if state != State.BROWSE:
            return
        if input == 'up':
            self.env.service.directory.scroll(-1)
            self.env.service.directory.view_file_or_folder()
        elif input == 'down':
            self.env.service.directory.scroll(1)
            self.env.service.directory.view_file_or_folder()
        elif input == 'n':
            self.env.service.state.new_note()
        elif input == 'N':
            self.env.service.state.new_folder()
        elif input == 'enter' or input == 'right':
            self.env.service.directory.open_folder_or_file()
        elif input == 'left':
            self.env.service.directory.leave_folder()
        elif input == 'g':
            self.env.service.state.search()