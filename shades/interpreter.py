from shades.config import BLACK, WHITE
from shades.conversions import to_hexcolor, to_rgba

stack = []
counter = 0
star = False

def reset_counter():
    global counter
    counter = 0

def inc_counter():
    global counter
    counter = counter + 1

def get_difference(a, b):
    if not a or not b:
        return 0
    (r_a, _, _, _) = to_rgba(a)
    (r_b, _, _, _) = to_rgba(b)
    return (r_a - r_b) / 16

def push():
    global counter
    stack.append(counter)
    reset_counter()

def number_out():
    print(str(stack[-1]))

def toggle_star():
    global star
    star = not star

def on_black():
    toggle_star()
    reset_counter()

def evaluate(previous, current):
    if not current:
        return None

    if not previous:
        return inc_counter

    if current == BLACK:
        return toggle_star

    difference = int(abs(get_difference(previous, current)))  # todo not abs
    if difference == 0:
        return inc_counter
    if difference == 1 and star == False:
        return push
    if difference == 6 and star == False:
        return number_out


def interpret(image):
    instructions = []
    i = 0
    previous = None
    while i < image.size[1]:
        current_rgb = image.getpixel((0, i))
        current_hex = to_hexcolor(current_rgb)

        if current_hex == WHITE:
            return instructions

        instruction = evaluate(previous, current_hex)
        if instruction != None:
            instructions.append(instruction)

        previous = current_hex
        i += 1

    return instructions


def execute(image):
    for instruction in interpret(image):
        instruction()
