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

    def handle_conversion_to_km(self):
        # print("test")
        miles_unit_conversion = 1.60934
        value = float(self.root.ids.user_input.text)
        result = value * miles_unit_conversion
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """
        increase/decrease the users input by the increment
        :param increment:
        :return:
        """
        result = int(self.root.ids.user_input.text) + increment
        self.root.ids.user_input.text = str(result)
        self.handle_conversion_to_km()


MilesConverter().run()
