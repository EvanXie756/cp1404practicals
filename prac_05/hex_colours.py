HEX_CODE = {"Absolute Zero": "#0048ba",
            "Acid Green": "#b0bf1a",
            "AliceBlue": "#f0f8ff",
            "Alizarin crimson": "#e32636",
            "Amaranth": "#e52b50",
            "Amber": "#ffbf00",
            "Amethyst": "#9966cc",
            "AntiqueWhite": "#faebd7",
            "Apricot": "#fbceb1"}

colour = input("Enter a colour name: ")
while colour != "":
    if colour in HEX_CODE:
        print(colour, "is", HEX_CODE[colour])
    else:
        print("Invalid colour")
    colour = input("Enter a colour name: ")
