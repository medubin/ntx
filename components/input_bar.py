class InputBar:
    def __init__(self, store, term):
        self.store = store
        self.term = term

    def render(self):
        if self.store.state == "NEW":
            with self.term.location(0, self.term.height - 1):
                print(self.store.write_buffer)





