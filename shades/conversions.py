# convert between hex and rgb

def to_hex(decimal):
    return hex(decimal)[2:].ljust(2, '0')

# # todo have this accept a tuple/ namedtuple
# def to_hexcolor(r, g, b):
#     return '#' + to_hex(r) + to_hex(g) + to_hex(b)

def to_hexcolor(rgb):
    return '#' + to_hex(rgb[0]) + to_hex(rgb[1]) + to_hex(rgb[2])

def to_rgb(hexstring):
    if not hexstring or (len(hexstring) != 6 and len(hexstring) != 7):
        return None
    hexstring = hexstring.strip('#')
    r, g, b = int(hexstring[:2], 16), int(hexstring[2:4], 16), int(hexstring[4:], 16)
    return (r, g, b)

def to_rgba(hexstring):
    rgb = to_rgb(hexstring)
    if not rgb:
        return None
    return (rgb[0], rgb[1], rgb[2], 255)
