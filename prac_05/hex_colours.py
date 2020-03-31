"""
Hexadecimal colour codes in a dictionary.
"""

HEX_COLOUR_CODES_DICT = {"DarkTurquoise": "#00ced1", "Maroon": "#b03060", "DarkGoldenrod1": "#ffb90f",
                         "Green1": "#00ff00", "GhostWhite": "#f8f8ff", "ForestGreen": "#228b22",
                         "Cyan1": "#00ffff", "DarkSalmon": "#e9967a", "Yellow1": "#ffff00", "Red1": "#ff0000"}

colour_name = input("Enter colour name: ").capitalize()

while colour_name != "":
    if colour_name in HEX_COLOUR_CODES_DICT:
        print(HEX_COLOUR_CODES_DICT[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")
