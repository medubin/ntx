import os
def get_files_in_folder(folder):
    return sorted([f for f in os.listdir(folder)], key=lambda f: f.lower())

def filter_hidden(files):
    return list(filter(lambda x: not x.startswith('.'), files))
