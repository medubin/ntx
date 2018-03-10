class Header:
    def __init__(self, store, term):
        self.store = store
        self.term = term
    
    def render(self):
        width = self.term.width
        padding = int((width - 3) / 2)
        print(self.term.green_on_blue(' ' * padding + 'ntx' + ' ' * padding))
