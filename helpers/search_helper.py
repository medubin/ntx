def search_files(search_string, files, base_directory):
    matches = []
    removal_length = len(base_directory) + 1
    for file in files:
        with open(file, 'r') as f:
            content = f.read()
            if search_string in content:
                matches.append(file[removal_length:])
    
    return matches
