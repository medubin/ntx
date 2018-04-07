import os
from base.base_service import BaseService

import helpers.delete_helper as delete_helper

class DeleteService(BaseService):        
    def folder_or_note(self, full_path):
        self.store.change_file_index(-1)
        if os.path.isdir(full_path):
            delete_helper.folder(full_path)
        else:
            delete_helper.note(full_path)
