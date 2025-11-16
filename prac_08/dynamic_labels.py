from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["John", "Joe", "Jason", "Mary", "Kevin", "Juan"]

    def build(self):
        self.root = Builder.load_file("dynamic_labels.kv")


