import markdown
import re
import urwid 

HEADER = {
        1: '#0f0',
        2: '#0d0',
        3: '#0a0',
        4: '#070',
        5: '#040',
        6: '#010'
}


def parse(text):
    line_split = text.split('\n')

    tags = __format_tags(line_split[0])

    line_split = list(map(lambda x: __format_markdown(x), line_split[1:])) 
    return [tags] + line_split



def __format_markdown(line):
    if len(line) == 0: # no need to format empty line
        return line
    line += '\n'
    return __format_headers(line) or line


def __format_tags(text):
    if len(text) == 0:
        return text

    if text[0] == '[' and text[-1] == ']':
        return (urwid.AttrSpec('#f00,bold', '', 256), 'tags: ' + text + '\n')
    
    return text

def __format_headers(line):
    headers = re.search(r'^\#+', line)
    if headers and len(headers.group(0)) < 7:
        h_number = len(headers.group(0))
        return (urwid.AttrSpec(HEADER[h_number] + ',bold', '', 256), line[h_number + 1:])
    return None

