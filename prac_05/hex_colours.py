"""
CP1404 Practical  Hex Colours
"""

COLOUR_CODES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}


def main():
    """Display hex codes for given colour names."""
    colour_name = input("Enter a colour name: ").strip()
    while colour_name != "":
        colour_code = COLOUR_CODES.get(colour_name.title())
        if colour_code:
            print(f"{colour_name.title()} is {colour_code}")
        else:
            print("Invalid colour name")
        colour_name = input("Enter a colour name: ").strip()


if __name__ == "__main__":
    main()
