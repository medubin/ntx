class FileContentService:

    def __init__(self, env):
        self.env = env

    def get(self, file):
        with self.open(file) as f:
            return self.env.service.markdown.parse_markdown(f.read())
    
    def open(self, file, type ='r'):
        return open(self.env.service.directory.base_directory + '/' + file, type)

        