import markdown
class FileViewerService:
    def __init__(self, term, store):
        self.store = store
        self.term = term

    
    def show_file(self, file_text):
        file_text_md = markdown.markdown(file_text)
        return file_text_md



    



