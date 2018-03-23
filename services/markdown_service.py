import markdown
from services.base_service import BaseService
class MarkdownService(BaseService):
    def __init__(self, env):
        self.env = env
    
    def parse(self, text):
        return markdown.markdown(text)



    



