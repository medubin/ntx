import pager
from input_listeners.browse_input import BrowseInput
from input_listeners.new_file_input import NewFileInput

class MasterInputListener:
    def __init__(self, store, service, components):
        self.store = store
        self.service = service
        self.components = components

        self.browse_input = BrowseInput(store, service, components)
        self.new_file_input = NewFileInput(store, service, components)

    def listen(self, input):
        state = self.store.state #freeze the state to prevent ordering errors
        self.browse_input.listen(input, state)
        self.new_file_input.listen(input, state)



