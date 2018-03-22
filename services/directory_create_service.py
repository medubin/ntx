import os


class DirectoryCreateService:

    def __init__(self, env):
        self.env = env
        
    def base_folder(self):
        if not os.path.isdir(self.env.service.directory.directory()):
            os.makedirs(self.env.service.directory.directory())

    def note(self):
        file = self.env.service.file_content.open(self.env.store.write_buffer + ".md","a") 
        file.close() 
        self.env.service.state.set_to_browse()
    
    def folder(self):
        directory = self.env.service.directory.directory() + '/' + self.env.store.write_buffer
        if not os.path.isdir(directory):
            os.makedirs(directory)
        self.env.service.state.set_to_browse()