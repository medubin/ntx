class Store:
    STATE_BROWSE = "BROWSE"
    STATE_NEW = "NEW"

    def __init__(self):
        self.opened_file = ''
        self.state = self.STATE_BROWSE
        self.write_buffer = ''
        self.selected_file = 0
        self.files = []
        