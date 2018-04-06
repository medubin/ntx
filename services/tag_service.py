from base.base_service import BaseService
import os


class TagService(BaseService):
    def get(self):
        tags = self.search_tags()
        self.store.set_tags(tags)
    
    def view(self):
        if self.store.get_selected_tag():
            self.view_file()
        else:
            self.view_tag_files()


    def view_tag_files(self):
        tag = list(self.store.get_tags().keys())[self.store.get_file_index()]
        tagged_files = self.store.get_tags()[tag]
        tagged_files = '\n'.join(tagged_files)
        self.component.open_file.widget.set_text(tagged_files)

    def view_file(self):
            tag = list(self.store.get_tags().keys())[self.store.get_file_index()]
            tagged_files = self.store.get_tags()[tag]
            file = tagged_files[self.store.get_file_index()]
            full_path = self.store.BASE_DIRECTORY + '/' + file
            self.service.file_content.view(full_path)





    def open_tag(self, tag):
        self.store.set_selected_tag(tag)
        tagged_files = self.store.get_tags()[tag]
        self.store.push_file_index(0)
        self.component.files.set_focus(0)
        self.component.files.content[:] = self.component.files.create_files(tagged_files)





    def search_tags(self):
        files = self.service.directory.all_files()
            
        all_tags = {}
        removal_length = len(self.store.BASE_DIRECTORY) + 1
        for file in files:
            with open(file, 'r') as f:
                first_line = f.readline() #just the first line
                tags = self.extract_tags(first_line)
                
                if not tags:
                    continue

                for tag in tags:
                    if tag in all_tags:
                        all_tags[tag].append(file[removal_length:])
                    else:
                        all_tags[tag] = [file[removal_length:]]
        
        return all_tags

    def extract_tags(self, text):
        text = text.strip()
        if len(text) == 0:
            return None

        if text[0] == '[' and text[-1] == ']':
            text = text[1:-2]
            return text.split(', ')
        return None
