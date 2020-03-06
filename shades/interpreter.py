from shades.config import BLACK, WHITE
from shades.conversions import to_hexcolor, to_rgba
from shades.instructions import on_black, inc_counter, push, pop, add, multiply, duplicate, number_out, char_out

class State:
    def __init__(self, stack=None, counter=1 , star=False):
        self.stack = stack if stack else []
        self.counter = counter
        self.star = star

def get_difference(a, b):
    if not a or not b:
        return 0
    (r_a, _, _, _) = to_rgba(a)
    (r_b, _, _, _) = to_rgba(b)
    return (r_a - r_b) / 16

def evaluate(state, previous, current):
    if not current or not previous:
        return None

    if current == BLACK:
        return on_black

    difference = int(get_difference(previous, current))
    print('difference: ' + str(difference))
    if difference == 0:
        return inc_counter

    if difference == 1 and not state.star:
        return push
    if difference == 1 and state.star:
        return pop
    if difference == 2 and not state.star:
        return add
    if difference == 3 and not state.star:
        return multiply
    if difference == 5 and state.star:
        return duplicate
    if difference == 6 and not state.star:
        return number_out
    if difference == 6 and state.star:
        return char_out


def interpret(image):
    state = State()

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

        instruction = evaluate(state, previous, current_hex)
        if instruction != None:
            print(instruction.__name__)
            state = instruction(state)

        print('counter: ' + str(state.counter))
        print(state.stack)

        previous = current_hex
        i += 1

    return instructions

