from base.base_service import BaseService
import os


class TagService(BaseService):
    def get(self):
        tags = self.search_tags()

        self.store.set_tags(tags)

    
    def search_tags(self):
        files = self.service.directory.all_files()
            
        all_tags = {}
        for file in files:
            with open(file, 'r') as f:
                first_line = f.readline() #just the first line
                tags = self.extract_tags(first_line)
                
                if not tags:
                    continue

                for tag in tags:
                    if tag in all_tags:
                        all_tags[tag].append(file)
                    else:
                        all_tags[tag] = [file]
        
        return all_tags

    def extract_tags(self, text):
        text = text.strip()
        if len(text) == 0:
            return None

        if text[0] == '[' and text[-1] == ']':
            text = text[1:-2]
            return text.split(', ')
        return None
