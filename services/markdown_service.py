import markdown
class MarkdownService:
    def __init__(self, term, store, service):
        self.store = store
        self.term = term
    
    def parse_markdown(self, text):
        return markdown.markdown(text)



    



