import os
from pathlib import Path

class DirectoryService:
    base_directory = str(Path.home()) + '/.ntx'

    def __init__(self, env):
        self.env = env
        self.env.store.files = os.listdir(self.base_directory)

    def get_selected_file(self):
        return self.env.store.files[self.env.store.selected_file]
