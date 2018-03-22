from stores.master_store import MasterStore
from components.master_component import MasterComponent
from input.master_input import MasterInput
from services.master_service import MasterService

class Env:
    def __init__(self):
        self.store = MasterStore()        
        self.service = MasterService(self)
        self.input = MasterInput(self)
        self.component = MasterComponent(self)
