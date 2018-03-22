class MasterStore:
    STATE_BROWSE = "BROWSE"
    STATE_NEW_FILE = "NEW_FILE"
    STATE_NEW_FOLDER = "NEW_FOLDER"

    def __init__(self):
        self.opened_file = '' #opened file contents
        self.state = self.STATE_BROWSE 
        self.write_buffer = ''
        self.selected_file = 0 #selected file index
        self.files = []
        self.directory = ''
        