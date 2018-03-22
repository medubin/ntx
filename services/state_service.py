import os
class StateService:
    def __init__(self, env):
        self.env = env

    def set_to_browse(self):
        self.env.store.write_buffer = ''
        self.env.store.files = os.listdir(self.env.service.directory.directory())
        self.env.store.state = self.env.store.STATE_BROWSE 
        self.env.component.input_bar.widget.set_text('')
        self.env.component.files.content[:] = self.env.component.files.create_files()
        self.env.component.files.widget.set_focus(0)



    
