"""
CP1404 prac_07
A simple kivy program that will allow a user to convert Miles to Kilometers.
"""
from kivy.app import App
from kivy.lang import Builder


class MilesConverter(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


MilesConverter().run()
