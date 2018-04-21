from ntx.input.browse_input import BrowseInput
from ntx.input.command_input import CommandInput
from ntx.input.search_result_input import SearchResultInput
from ntx.input.tags_input import TagsInput

class MasterInput:
    def __init__(self, env):
        self.env = env

        self.browse = BrowseInput(env)
        self.search_result = SearchResultInput(env)
        self.command = CommandInput(env)
        self.tags = TagsInput(env)

    def setup(self):
        self.browse.setup()
        self.search_result.setup()
        self.command.setup()
        self.tags.setup()


    def listen(self, input):
        state = self.env.component.get_state() #freeze the state to prevent ordering errors
        self.browse.listen(input, state)
        self.search_result.listen(input, state)
        self.command.listen(input, state)
        self.tags.listen(input, state)



