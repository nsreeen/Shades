from os import path
from PIL import Image, ImageDraw
from shades.config import height, WHITE, width
from shades.conversions import to_hexcolor

def get_first_white_y(image):
    current = 0
    while current < image.size[1]:
        pixel = image.getpixel((0, current))
        if to_hexcolor(pixel) == WHITE:
            return current
        current += 1
    return current

def create_new_program(name):
    image = Image.new('RGBA', (width, height), color=WHITE)
    image.save(name, "PNG")
    return image

def extend_program(filename, color):
    if not path.exists(filename):
        create_new_program(filename)

    image = Image.open(filename)
    draw = ImageDraw.Draw(image)

    target = get_first_white_y(image)

    draw.line((0, target, width, target), fill = color)
    image.save(filename, "PNG")