import urwid
class InputBar:
    def __init__(self, env):
        self.env = env
        self.widget = self.__render()

    def __render(self):
        return urwid.Text(('input', u''))

    def set_text(self, text):
        self.widget.set_text([self.env.store.input_state, ('input', text)])









