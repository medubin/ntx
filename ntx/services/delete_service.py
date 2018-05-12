import os
from ntx.base.base_service import BaseService

import ntx.helpers.delete_helper as delete_helper

class DeleteService(BaseService):        
    def folder_or_note(self, full_path):
        self.component.navigation.scroll(-1)
        if os.path.isdir(full_path):
            delete_helper.folder(full_path)
        else:
            delete_helper.note(full_path)
