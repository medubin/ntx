import markdown
class MarkdownService:
    def __init__(self, env):
        self.env = env
    
    def parse_markdown(self, text):
        return markdown.markdown(text)



    



