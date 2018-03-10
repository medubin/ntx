class OpenFile:
    def __init__(self, store, term):
        self.store = store
        self.term = term

    def render(self):
        if self.store.opened_file is not None:
            with self.term.location(0, self.term.height - int(self.term.height/2)):
                print(self.store.opened_file)