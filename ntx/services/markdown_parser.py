import re
import urwid
import markdown

HEADER = {
        1: '#0f0',
        2: '#0d0',
        3: '#0a0',
        4: '#070',
        5: '#040',
        6: '#010'
}



class MarkdownParser:
    def __init__(self):
        self.text = ''
        self.all_text = []
        self.current_text_block = ""
        self.tag = ''
        self.skip = False
        self.pos = 0
        self.header = 0
        self.italic = 0
        self.bold = 0

    def parse(self, text):
        if text == '':
            return text
        # return markdown.markdown(text)
        self.reset_state()
        self.text = text
        self.highlight_tags()
        self.add_escape_characters()
        self.text = markdown.markdown(self.text)
        self.format_html()
        
        return self.all_text

    def highlight_tags(self):
        text = self.text.split('\n')
        first_line = text[0]

        if first_line[0] == '[' and first_line[-1] == ']':
            self.all_text.append((urwid.AttrSpec('#f00,bold', '', 256), 'tags: ' + first_line[1:-2] + '\n'))
            self.text = '\n'.join(text[1:])

    def add_escape_characters(self):
        new_text = ''
        for char in self.text:
            if (char in ['/', '<', '>']):
                new_text += '/' + char
            else:
                new_text += char
        
        self.text = new_text

    def format_html(self):
        while self.pos < len(self.text):
            if self.skip:
                self.skip = False

            
            elif self.text[self.pos] == '<':
                self.get_tag()
                self.style_section()
                self.implement_tag()
                self.clear_after_tag()

            else:
                self.current_text_block += self.text[self.pos]


            
            self.pos += 1

    def get_tag(self,):
        for i in range(self.pos, len(self.text)):
            self.tag += self.text[i]
            if self.text[i] == '>':
                self.pos = i
                return
    
    def style_section(self):
        styles = []
        if self.header:
            styles.append(HEADER[self.header])
        
        if self.italic:
            styles.append('italics')
        if self.bold:
            styles.append('bold')
        
        style_string = ','.join(styles)

        block = (urwid.AttrSpec(style_string, '', 256), self.current_text_block)

        self.all_text.append(block)

    def clear_after_tag(self):
        self.tag = ''
        self.current_text_block = ''

    def reset_state(self):
        self.text = ''
        self.all_text = []
        self.current_text_block = ""
        self.tag = ''
        self.skip = False
        self.pos = 0
        self.header = 0
        self.italic = 0
        self.bold = 0

    def implement_tag(self):
        if self.tag == '<p>':
            return
        elif self.tag == '</p>':
            self.text += "\n"
        elif self.tag == '<em>':
            self.italic += 1
        elif self.tag == '</em>':
            self.italic -= 1
        elif self.tag == '<strong>':
            self.bold += 1
        elif self.tag == '</strong>':
            self.bold -= 1
        elif self.tag.startswith('<h'):
            self.header = int(self.tag[2])
        elif self.tag.startswith('</h'):
            self.header = 0