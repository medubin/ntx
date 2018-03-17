import markdown
class MarkdownService:
    def __init__(self, store, service):
        self.store = store
    
    def parse_markdown(self, text):
        return markdown.markdown(text)



    



