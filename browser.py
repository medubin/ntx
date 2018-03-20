from store import Store
import time
import urwid
from components.master_component import MasterComponent
from input_listeners.master_input_listener import MasterInputListener
from services.master_service import MasterService

class Browser:
    def __init__(self):
        self.store = Store()
        self.service = MasterService(self.store)
        self.master_component = MasterComponent(self.store)
        self.master_input_listener = MasterInputListener(self.store, self.service, self.master_component)

    def startup(self):
        self.service.directory_service.create_base_directory()

    def run(self):
        self.master_component.run(self.master_input_listener)

    def __input_filter(self, input, raw):
        return input
