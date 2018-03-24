import urwid
from base.base_component import BaseComponent
class InputBar(BaseComponent):
    def __init__(self, env):
        self.env = env
        self.widget = self.__render()

    def __render(self):
        return urwid.Text(('input', u''))

    def set_text(self, text):
        self.widget.set_text([self.store.input_state, ('input', text)])









