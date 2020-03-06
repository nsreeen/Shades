from shades.config import BLACK, WHITE
from shades.conversions import to_hexcolor, to_rgba

stack = []
counter = 1
star = False

def reset_counter():
    global counter
    counter = 1

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

def pop():
    return stack.pop()

def add():
    a = stack.pop()
    b = stack.pop()
    return stack.append(a + b)

def multiply():
    a = stack.pop()
    b = stack.pop()
    return stack.append(a * b)

def duplicate():
    stack.append(stack[-1])

def number_out():
    print(str(stack[-1]))

def char_out():
    print(chr(stack[-1]))

def toggle_star():
    global star
    star = not star

def on_black():
    toggle_star()
    reset_counter()

def evaluate(previous, current):
    if not current or not previous:
        return None

    if current == BLACK:
        return on_black

    difference = int(get_difference(previous, current))
    print('difference: ' + str(difference))
    if difference == 0:
        return inc_counter

    if difference == 1 and not star:
        return push
    if difference == 1 and star:
        return pop
    if difference == 2 and not star:
        return add
    if difference == 3 and not star:
        return multiply
    if difference == 5 and star:
        return duplicate
    if difference == 6 and not star:
        return number_out
    if difference == 6 and star:
        return char_out


def interpret(image):
    instructions = []
    i = 0
    previous = None
    while i < image.size[1]:
        print('\n')
        current_rgb = image.getpixel((0, i))
        current_hex = to_hexcolor(current_rgb)
        print(current_hex)

        if current_hex == WHITE:
            break

        instruction = evaluate(previous, current_hex)
        if instruction != None:
            print(instruction.__name__)
            instruction()

        print('counter: ' + str(counter))
        print(stack)

        previous = current_hex
        i += 1

    return instructions

