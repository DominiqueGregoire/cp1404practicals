"""
CP1404 prac_07
A simple kivy program that will allow a user to convert Miles to Kilometers.
"""
from kivy.app import App
from kivy.lang import Builder

MILES_UNIT_CONVERSION = 1.60934


class MilesConverter(App):
    def build(self):
        """
        Initiates the MilesConverter class
        :return: self
        """
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_conversion_to_km(self):
        """
        Convert a given user input of miles to kilometers
        :return: none
        """
        # print("test")

        # value = float(self.root.ids.user_input.text)
        value = float(self.handle_invalid_inputs())
        result = value * MILES_UNIT_CONVERSION
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """
        Increase/decrease the users input by the increment
        :param increment:
        :return: none
        """
        # result = int(self.root.ids.user_input.text) + increment
        result = self.handle_invalid_inputs() + increment
        self.root.ids.user_input.text = str(result)
        self.handle_conversion_to_km()

    def handle_invalid_inputs(self):
        """
        Check whether user inputs are valid
        :return: valid user input or 0 if invalid
        """
        try:
            value = float(self.root.ids.user_input.text)
            return value
        except ValueError:
            return 0


MilesConverter().run()
