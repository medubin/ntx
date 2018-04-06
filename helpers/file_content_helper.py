import helpers.markdown_helper as markdown
def get(file):
    with open_note(file) as f:
        return markdown.parse(f.read())

def open_note(file, type ='r'):
    return open(file, type)




