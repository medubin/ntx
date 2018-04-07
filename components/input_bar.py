import urwid
class InputBar:
    def __init__(self, env):
        self.env = env
        self.widget = self.__render()

        self.__text = ''
        self.__pos = 0 #distance from the end

    def __render(self):
        return urwid.Text(('input', u''))

    def set_display(self, text):
        cursor_pos_from_left = len(text) - self.__pos

        if len(text) == 0:
            display = ('input cursor', ' ')
        elif self.__pos == 0:
            display = [('input', text), ('input cursor', ' ')]      
        elif cursor_pos_from_left == 0:
            display = [('input cursor', text[cursor_pos_from_left]), ('input', text[cursor_pos_from_left + 1:])]  
        else:
            display = [('input', text[:cursor_pos_from_left]), ('input cursor', text[cursor_pos_from_left]), ('input', text[cursor_pos_from_left + 1:])]  

        self.widget.set_text([self.env.store.input_state, display])


    def scroll(self, velocity):
        if 0 <= (self.get_pos() + velocity) <= len(self.get_text()):
            self.change_pos(velocity)
            self.set_display(self.get_text())
    
    def insert_char(self, char):
        self.insert_text(char, self.get_pos_from_front())
        self.set_display(self.get_text())

    def splice_char(self):
        self.splice_text(self.get_pos_from_front())
        self.set_display(self.get_text())



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



    #pos
    def get_pos(self):
        return self.__pos
    
    def get_pos_from_front(self):
        return len(self.get_text()) -  self.get_pos()
    
    def set_pos(self, pos):
        self.__pos = pos
    
    def change_pos(self, velocity):
        self.__pos += velocity










