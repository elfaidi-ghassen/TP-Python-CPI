colors = {
    "red": "#ff0000",
    "green": "#00ff00",
    "blue": "#0000ff"
}

color = input("type a color name: ")
if color.lower() in colors.keys():
    print(f"The color code is {colors[color.lower()]}")
else:
    print("Unknown color")