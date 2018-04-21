
from ntx.master.master_component import MasterComponent
from ntx.master.master_input import MasterInput
from ntx.master.master_service import MasterService

class Env:
    def __init__(self):
        self.component = MasterComponent(self)   
        self.service = MasterService(self)
        self.input = MasterInput(self)

        self.service.setup()
        self.input.setup()
        
