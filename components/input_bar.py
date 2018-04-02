import urwid
class InputBar:
    def __init__(self, env):
        self.env = env
        self.widget = self.__render()

    def __render(self):
        return urwid.Text(('input', u''))

    def set_text(self, text):
        cursor_pos =  self.env.store.get_write_cursor_pos()
        cursor_pos_from_left = len(text) - cursor_pos

        if len(text) == 0:
            display = ('input cursor', ' ')
        elif cursor_pos == 0:
            display = [('input', text), ('input cursor', ' ')]      
        elif cursor_pos_from_left == 0:
            display = [('input cursor', text[cursor_pos_from_left]), ('input', text[cursor_pos_from_left + 1:])]  
        else:
            display = [('input', text[:cursor_pos_from_left]), ('input cursor', text[cursor_pos_from_left]), ('input', text[cursor_pos_from_left + 1:])]  

        self.widget.set_text([self.env.store.input_state, display])









