from base.base_service import BaseService
import os

import helpers.tag_helper as tag_helper

class TagService(BaseService):
    def get(self):
        files = self.service.directory.all_files()
        base_directory = self.component.navigation.BASE_DIRECTORY
        tags = tag_helper.search_tags(files,  base_directory)
        self.store.set_tags(tags)
    
    def view(self):
        if self.store.get_selected_tag():
            self.view_file()
        else:
            self.view_tag_files()


    def view_tag_files(self):
        tag = list(self.store.get_tags().keys())[self.component.navigation.get_file_index()]
        tagged_files = self.store.get_tags()[tag]
        tagged_files = '\n'.join(tagged_files)
        self.component.display.widget.set_text(tagged_files)

    def view_file(self):
            tag = list(self.store.get_tags().keys())[self.component.navigation.get_file_index()]
            tagged_files = self.store.get_tags()[tag]
            file = tagged_files[self.component.navigation.get_file_index()]
            full_path = self.component.navigation.BASE_DIRECTORY + '/' + file
            self.service.file_content.view(full_path)


    def open_tag(self, tag):
        self.store.set_selected_tag(tag)
        tagged_files = self.store.get_tags()[tag]
        self.component.navigation.push_file_index(0)
        self.component.navigation.set_focus(0)
        self.component.navigation.content[:] = self.component.navigation.create_files(tagged_files)
    
    def leave_tag(self):
        if not self.store.get_selected_tag():
            return 

        self.component.navigation.pop_file_index()
        self.store.set_selected_tag(None)
        self.component.navigation.content[:] = self.component.navigation.create_files(self.store.get_tags().keys())
        self.component.navigation.set_focus(self.component.navigation.get_file_index()) 





   
