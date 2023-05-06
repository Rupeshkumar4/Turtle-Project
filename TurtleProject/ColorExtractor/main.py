import colorgram

rgb_colors = []

colors = colorgram.extract('hirst.jpg',30)

for color in colors:
    # rgb_colors.append(color.rgb)
    
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)

