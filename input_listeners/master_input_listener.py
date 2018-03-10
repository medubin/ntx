import pager
from input_listeners.browse_input import BrowseInput
from input_listeners.new_file_input import NewFileInput

class MasterInputListener:
    def __init__(self, store, term, service):
        self.store = store
        self.term = term
        self.service = service

        self.browse_input = BrowseInput(store, term, service)
        self.new_file_input = NewFileInput(store, term, service)

    def listen(self):
        input = pager.getchars()
        self.dispatch(input)

    def dispatch(self, input):
        state = self.store.state #freeze the state to prevent ordering errors
        self.browse_input.listen(input, state)
        self.new_file_input.listen(input, state)






