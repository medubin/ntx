class Files:
    def __init__(self, store, term):
        self.store = store
        self.term = term

    def render(self):
        for index, file in enumerate(self.store.files):
            if index == self.store.selected_file:
                print(self.term.bold_on_green(file))
            else:
                print(self.term.bold(file))


