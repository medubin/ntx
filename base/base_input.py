class BaseInput:
    def __init__(self, env):
        self.env = env
    
    def setup(self):
        self.service = self.env.service
        self.component = self.env.component
        self.env = None
