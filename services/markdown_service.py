import markdown
# from pygments import highlight
# from pygments.lexers import HtmlLexer
# from pygments.formatters import TerminalTrueColorFormatter

import re
import urwid


import urwid 
from base.base_service import BaseService
class MarkdownService(BaseService):
    HEADER = {
        1: '#0f0',
        2: '#0d0',
        3: '#0a0',
        4: '#070',
        5: '#040',
        6: '#010'
    }

    # mdv.term_columns = 30

# calling like this (all CLI options supported, check def main

    def parse(self, text):
        line_split = text.split('\n')

        tags = self.__tags(line_split[0])

        line_split = list(map(lambda x: self.__format_markdown(x), line_split[1:])) 
        return [tags] + line_split



    def __format_markdown(self, line):
        if len(line) == 0: # no need to format empty line
            return line
        line += '\n'
        return self.__headers(line) or line


    def __tags(self, text):
        if len(text) == 0:
            return text

        if text[0] == '[' and text[-1] == ']':
            return (urwid.AttrSpec('#f00,bold', '', 256), text)
        
        return text

    def __headers(self, line):
        headers = re.search(r'^\#+', line)
        if headers and len(headers.group(0)) < 7:
            h_number = len(headers.group(0))
            return (urwid.AttrSpec(self.HEADER[h_number] + ',bold', '', 256),line[h_number + 1:])
        return None

        
    