from input.browse_input import BrowseInput
from input.new_file_input import NewFileInput
from input.search_input import SearchInput
from input.search_result_input import SearchResultInput

class MasterInput:
    def __init__(self, env):
        self.env = env

        self.browse = BrowseInput(env)
        self.new_file = NewFileInput(env)
        self.search = SearchInput(env)
        self.search_result = SearchResultInput(env)

    def listen(self, input):
        state = self.env.store.state #freeze the state to prevent ordering errors
        self.browse.listen(input, state)
        self.new_file.listen(input, state)
        self.search.listen(input, state)
        self.search_result.listen(input, state)



