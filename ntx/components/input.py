import urwid
class Input:
    def __init__(self, env):
        self.env = env
        self.widget = self.__render()

        self.__text = ''
        self.__pos = 0 #distance from the end
        self.__prefix = ''

    def __render(self):
        return urwid.Text(('input', u''))

    def reset(self, text='', prefix='', pos=0):
        self.set_text(text)
        self.set_prefix(prefix)
        self.set_pos(pos)
        self.update_display()

    def update_display(self):
        cursor_pos_from_left = len(self.__text) - self.__pos

        if len(self.__text) == 0:
            display = ('input cursor', ' ')
        elif self.__pos == 0:
            display = [('input', self.__text), ('input cursor', ' ')]      
        elif cursor_pos_from_left == 0:
            display = [('input cursor', self.__text[cursor_pos_from_left]), ('input', self.__text[cursor_pos_from_left + 1:])]  
        else:
            display = [('input', self.__text[:cursor_pos_from_left]), ('input cursor', self.__text[cursor_pos_from_left]), ('input', self.__text[cursor_pos_from_left + 1:])]  

        self.widget.set_text([self.get_prefix(), display])


    def scroll(self, velocity):
        if 0 <= (self.get_pos() + velocity) <= len(self.get_text()):
            self.change_pos(velocity)
            self.update_display()
    
    def insert_char(self, char):
        self.insert_text(char, self.get_pos_from_front())
        self.update_display()

    def splice_char(self):
        self.splice_text(self.get_pos_from_front())
        self.update_display()



    # REGION GETTERS AND SETTER

    #text
    def get_text(self):
        return self.__text
    
    def set_text(self, text):
        self.__text = text
    
    def push_text(self, char):
        self.__text += char
    
    def pop_text(self):
        self.__text = self.__text[:-1]

    def insert_text(self, char, pos):
        self.__text = self.__text[:pos] + char + self.__text[pos:]

    def splice_text(self, pos):
        if(pos == 0):
            return
            
        self.__text = self.__text[:pos - 1] + self.__text[pos:]

    #prefix
    def get_prefix(self):
        return self.__prefix

    def set_prefix(self, prefix):
        self.__prefix = prefix



    #pos
    def get_pos(self):
        return self.__pos
    
    def get_pos_from_front(self):
        return len(self.get_text()) -  self.get_pos()
    
    def set_pos(self, pos):
        self.__pos = pos
    
    def change_pos(self, velocity):
        self.__pos += velocity










