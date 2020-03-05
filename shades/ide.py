from os import path
from PIL import Image, ImageDraw
from shades.config import height, filename, WHITE, width
from shades.conversions import to_hexcolor

def get_first_white_y(image):
    current = 0
    while current < image.size[1]:
        pixel = image.getpixel((0, current))
        if to_hexcolor(pixel) == WHITE:
            return current
        current += 1
    return current

def create_and_save_new_image():
    image = Image.new('RGBA', (width, height), color=WHITE)
    image.save(filename, "PNG")
    return image

def extend_program(color):
    if not path.exists(filename):
        create_and_save_new_image()

    image = Image.open(filename)
    draw = ImageDraw.Draw(image)

    target = get_first_white_y(image)

    draw.line((0, target, width, target), fill = color)
    image.save(filename, "PNG")