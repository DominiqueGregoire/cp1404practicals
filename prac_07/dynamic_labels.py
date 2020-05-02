"""
CP1404 Prac_07
Simple app that has a list of names and displays each one as a separate label
"""

from kivy.app import App
from kivy.app import Widget


# from kivy.lang import Builder


class DynamicLabels(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Widget()
        return self.root


DynamicLabels().run()
