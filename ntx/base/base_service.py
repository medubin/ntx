class BaseService:
    def __init__(self, env):
        self.env = env
    
    def setup(self):
        self.component = self.env.component
        self.service = self.env.service
        self.env = None
