"""
CP1404 Prac_07
Simple app that has a list of names and displays each one as a separate label
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.app import StringProperty


class DynamicLabels(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Bob", "Suzy", "cat", "dog"]  # use a string of names to test the widget

    def build(self):
        """Build the Dynamic Labels GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create the labels and add them to the GUI"""
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.add_widget(temp_label)


DynamicLabels().run()
