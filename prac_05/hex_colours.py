"""
Hexadecimal colour codes in a dictionary.
"""

HEX_COLOUR_CODES_DICT = {"DarkTurquoise": "#00ced1", "maroon": "#b03060", "DarkGoldenrod1": "#ffb90f",
                         "green1": "#00ff00", "GhostWhite": "#f8f8ff", "ForestGreen": "#228b22",
                         "cyan1": "#00ffff", "DarkSalmon": "#e9967a", "yellow1": "#ffff00", "red1": "#ff0000"}

#  create a copy of the HEX_COLOUR_CODES_DICT to be able to handle various key inputs by user
copied_colour_dict = {}
for colour in HEX_COLOUR_CODES_DICT:
    capitalised_colour = colour.capitalize()  # to handle capitalised inputs
    copied_colour_dict[capitalised_colour] = HEX_COLOUR_CODES_DICT[colour]
    case_folded_colour = colour.casefold()  # to handle all lowercase inputs
    copied_colour_dict[case_folded_colour] = HEX_COLOUR_CODES_DICT[colour]

colour_name = input("Enter colour name: ").capitalize()

while colour_name != "":
    if colour_name in copied_colour_dict:
        print(copied_colour_dict[colour_name])
    elif colour_name in HEX_COLOUR_CODES_DICT:
        print(HEX_COLOUR_CODES_DICT[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")
