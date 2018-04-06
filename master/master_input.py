from input.browse_input import BrowseInput
from input.new_file_input import NewFileInput
from input.search_input import SearchInput
from input.search_result_input import SearchResultInput
from input.delete_input import DeleteInput
from input.command_input import CommandInput
from input.tags_input import TagsInput

class MasterInput:
    def __init__(self, env):
        self.env = env

        self.browse = BrowseInput(env)
        self.new_file = NewFileInput(env)
        self.search = SearchInput(env)
        self.search_result = SearchResultInput(env)
        self.delete = DeleteInput(env)
        self.command = CommandInput(env)
        self.tags = TagsInput(env)

    def setup(self):
        self.browse.setup()
        self.new_file.setup()
        self.search.setup()
        self.search_result.setup()
        self.delete.setup()
        self.command.setup()
        self.tags.setup()


    def listen(self, input):
        state = self.env.store.state #freeze the state to prevent ordering errors
        self.browse.listen(input, state)
        self.new_file.listen(input, state)
        self.search.listen(input, state)
        self.search_result.listen(input, state)
        self.delete.listen(input, state)
        self.command.listen(input, state)
        self.tags.listen(input, state)



