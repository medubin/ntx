from blessings import Terminal
from store import Store
import time

from components.master_component import MasterComponent
from input_listeners.master_input_listener import MasterInputListener
from services.master_service import MasterService

class Browser:
    def __init__(self):
        self.term = Terminal()
        self.store = Store()

        self.master_component = MasterComponent(self.store, self.term)
        self.service = MasterService(self.store, self.term)
        self.master_input_listener = MasterInputListener(self.store, self.term, self.service)
        
    def startup(self):
        self.service.directory_service.create_base_directory()
        print(self.term.enter_fullscreen())

    def exit(self):
        print(self.term.clear)
        print(self.term.exit_fullscreen)

    def run(self):
        while(True):
            self.__print()
            # time.sleep(.5)

    def __print(self):
        print(self.term.clear)
        self.master_component.render()
        self.master_input_listener.listen()
            
    


