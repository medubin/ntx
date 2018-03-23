
from stores.master_store import MasterStore
from master.master_component import MasterComponent
from master.master_input import MasterInput
from master.master_service import MasterService

class Env:
    def __init__(self):
        self.store = MasterStore()     
        self.component = MasterComponent(self)   
        self.service = MasterService(self)
        self.input = MasterInput(self)

        self.service.setup()
        self.input.setup()
        
