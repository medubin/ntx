from services.directory_service import DirectoryService

class MasterService:
    def __init__(self, store, term):
        self.store = store
        self.term = term

        self.directory_service = DirectoryService(store, term, self)