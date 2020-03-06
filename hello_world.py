from shades.adjustcolors import darken_color
from shades.config import BLACK
from shades.ide import create_new_program, extend_program


def create_program(filename, starting_color):
    create_new_program(filename)

    # h
    for i in range(10): # count 10
        extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 1)) # push
    extend_program(filename, BLACK) # toggle start ON & reset counter
    extend_program(filename, starting_color) # starting point for shade change
    extend_program(filename, darken_color(starting_color, 5)) # duplicate
    extend_program(filename, BLACK) # toggle start OFF & reset counter
    extend_program(filename, starting_color) # starting point for shade change
    extend_program(filename, darken_color(starting_color, 3)) # multiply
    extend_program(filename, BLACK) # reset counter and shade starting point
    extend_program(filename, BLACK)
    for i in range(4): # count 4
        extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 1)) # push
    extend_program(filename, darken_color(starting_color, 3)) # add
    extend_program(filename, BLACK) # toggle start ON & reset counter
    extend_program(filename, starting_color) # starting point for shade change
    extend_program(filename, darken_color(starting_color, 6)) # print char

    # e
    extend_program(filename, BLACK) # toggle OFF
    for i in range(3): # count 3
        extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 1)) # push
    extend_program(filename, BLACK) # toggle ON
    extend_program(filename, starting_color) # starting point for shade change
    extend_program(filename, darken_color(starting_color, 2)) # subtract
    extend_program(filename, darken_color(starting_color, 8)) # print char

    # l
    extend_program(filename, BLACK) # toggle OFF
    for i in range(7): # count 7
        extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 1)) # push
    extend_program(filename, darken_color(starting_color, 3)) # add
    extend_program(filename, BLACK) # toggle ON
    extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 6)) # print l
    extend_program(filename, darken_color(starting_color, 12)) # print l

    # o
    extend_program(filename, BLACK) # toggle OFF
    for i in range(3): # count 3
        extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 1)) # push
    extend_program(filename, darken_color(starting_color, 3)) # add
    extend_program(filename, BLACK) # toggle ON
    extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 6)) # print o

    # push 'world to stack in opposite order: 100 108 114 111 119
    extend_program(filename, BLACK) # toggle OFF
    for i in range(11): # count 11
        extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 1)) # push 111 11
    extend_program(filename, BLACK) # toggle ON
    extend_program(filename, starting_color) # starting point for shade change
    extend_program(filename, darken_color(starting_color, 2)) # subtract 100
    extend_program(filename, darken_color(starting_color, 7)) # dup 100 100
    extend_program(filename, darken_color(starting_color, 12)) #dup 100 100 100
    extend_program(filename, BLACK) # toggle OFF
    for i in range(8): # count 8
        extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 1)) # push 100 100 100 8
    extend_program(filename, darken_color(starting_color, 3)) # add 100 100 108
    extend_program(filename, darken_color(starting_color, 10)) # swap 100 108 100
    for i in range(10): # count 10 more
        extend_program(filename, darken_color(starting_color, 10))
    extend_program(filename, darken_color(starting_color, 11)) # push 100 108 100 11
    extend_program(filename, darken_color(starting_color, 13)) # add 100 108 111
    extend_program(filename, BLACK) # toggle ON
    extend_program(filename, starting_color) # starting point for shade change
    extend_program(filename, darken_color(starting_color, 5)) # dup 100 108 111 111
    extend_program(filename, BLACK) # toggle OFF
    for i in range(3): # count 3
        extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 1)) # push 100 108 111 111 3
    extend_program(filename, darken_color(starting_color, 3)) # add  100 108 111 114
    extend_program(filename, darken_color(starting_color, 10)) # swap 100 108 114 111
    extend_program(filename, BLACK) # toggle ON
    extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 5)) # dup 100 108 114 111 111
    extend_program(filename, BLACK) # toggle OFF
    for i in range(8): # count 8
        extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 1)) # push 100 108 114 111 111 8
    extend_program(filename, darken_color(starting_color, 3)) # add  100 108 114 111 119
    extend_program(filename, BLACK) # toggle ON
    extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 6)) # print w
    extend_program(filename, darken_color(starting_color, 7)) # pop
    extend_program(filename, BLACK) # toggle OFF
    extend_program(filename, BLACK) # toggle ON
    extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 6)) # print o
    extend_program(filename, darken_color(starting_color, 7)) # pop
    extend_program(filename, BLACK) # toggle OFF
    extend_program(filename, BLACK) # toggle ON
    extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 6)) # print r
    extend_program(filename, darken_color(starting_color, 7)) # pop
    extend_program(filename, BLACK) # toggle OFF
    extend_program(filename, BLACK) # toggle ON
    extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 6)) # print l
    extend_program(filename, darken_color(starting_color, 7)) # pop
    extend_program(filename, BLACK) # toggle OFF
    extend_program(filename, BLACK) # toggle ON
    extend_program(filename, starting_color)
    extend_program(filename, darken_color(starting_color, 6)) # print d
    extend_program(filename, darken_color(starting_color, 7)) # pop