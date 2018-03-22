
class FileContentService:
    def __init__(self, env):
        self.env = env

    def get(self, file):
        with self.open(file) as f:
            return self.env.service.markdown.parse_markdown(f.read())
    
    def open(self, file, type ='r'):
        return open(self.env.service.directory.directory() + '/' + file, type)


    def view(self):
        file = self.env.service.directory.get_selected_file()
        if (file is not None):
            self.env.store.opened_file = self.env.service.file_content.get(file)
            self.env.component.open_file.widget.set_text(self.env.store.opened_file)

        