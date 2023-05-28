import json

with open("colors.json", "r") as file:
    data = json.load(file)

colors = []
for color in data["colors"]:
    updated_color = {}
    updated_color["color"] = color["color"]
    rgb = color["code"]["rgba"][:-1]
    updated_color["rgb"] = ", ".join([str(x) for x in rgb])
    updated_color["hex"] = color["code"]["hex"]
    colors.append(updated_color)

with open("colors_two.json", "w") as file:
    json.dump(colors, file, indent=1)
