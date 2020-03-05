# adjust hex colors

def normalise(val, minimum=0, maximum=255):
    if val < minimum:
        return minimum
    if val > maximum:
        return maximum
    return val

def adjust_color(hex_string, change):
    hex_string = hex_string.strip('#')
    if len(hex_string) != 6:
        return hex_string
    r, g, b = int(hex_string[:2], 16), int(hex_string[2:4], 16), int(hex_string[4:], 16)
    r = normalise(r + change)
    g = normalise(g + change)
    b = normalise(b + change)
    return "#%02x%02x%02x" % (r, g, b)

def darken_color(color, steps):
    for i in range(steps):
        color = adjust_color(color, -16)
    return color

def lighten_color(color, steps):
    for i in range(steps):
        color = adjust_color(color, 16)
    return color
