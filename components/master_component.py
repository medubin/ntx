from components.files import Files
from components.input_bar import InputBar
from components.open_file import OpenFile

class MasterComponent:
    def __init__(self, store, term):
        self.store = store
        self.term = term

        self.files = Files(store, term)
        self.input_bar = InputBar(store, term)
        self.open_file = OpenFile(store, term)
    
    def render(self):
        self.files.render()
        self.input_bar.render()
        self.open_file.render()
