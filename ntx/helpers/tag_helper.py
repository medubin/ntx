import ntx.helpers.directory_helper as directory_helper
def search_tags(files, base_directory):
    all_tags = {}
    removal_length = len(base_directory) + 1
    files = directory_helper.filter_hidden(files)
    for file in files:
        with open(file, 'r') as f:
            first_line = f.readline() #just the first line
            tags = extract_tags(first_line)
            
            if not tags:
                continue

            for tag in tags:
                if tag in all_tags:
                    all_tags[tag].append(file[removal_length:])
                else:
                    all_tags[tag] = [file[removal_length:]]
    
    return all_tags


def extract_tags(text):
    text = text.strip()
    if len(text) == 0:
        return None

    if text[0] == '[' and text[-1] == ']':
        text = text[1:-2]
        return text.split(', ')
    return None
