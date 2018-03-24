class BaseComponent:
    def __init__(self, env):
        self.env = env
    
    def setup(self):
        self.store = self.env.store
