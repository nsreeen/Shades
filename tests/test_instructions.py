from shades.instructions import on_black, inc_counter, push, pop, add, mul, sub, div, mod, dup, not_, greq
from shades.interpreter import State


class TestInstructions():

    def test_on_black(self):
        state = on_black(State(counter=4))
        assert state.counter == 1
        assert state.star == True

    def test_inc_counter(self):
        state = inc_counter(State())
        assert state.counter == 2

    def test_push(self):
        state = push(State())
        assert len(state.stack) == 1
        assert state.stack[0] == 1

    def test_pop(self):
        state = pop(State(stack=[1]))
        assert len(state.stack) == 0

    def test_add(self):
        state = add(State(stack=[2, 3]))
        assert len(state.stack) == 1
        assert state.stack[0] == 5

    def test_mul(self):
        state = mul(State(stack=[2, 3]))
        assert len(state.stack) == 1
        assert state.stack[0] == 6

    def test_sub(self):
        state = sub(State(stack=[10, 4]))
        assert len(state.stack) == 1
        assert state.stack[0] == 6

    def test_div(self):
        state = div(State(stack=[6, 2]))
        assert len(state.stack) == 1
        assert state.stack[0] == 3

    def test_mod(self):
        state = mod(State(stack=[5, 2]))
        assert len(state.stack) == 1
        assert state.stack[0] == 1

    def test_dup(self):
        state = dup((State(stack=[1])))
        assert len(state.stack) == 2
        assert state.stack[0] == 1
        assert state.stack[1] == 1

    def test__not(self):
        state = not_(State(stack=[3]))
        assert len(state.stack) == 1
        assert state.stack[0] == -3

    def test__greq(self):
        state = greq(State(stack=[3, 1]))
        assert len(state.stack) == 1
        assert state.stack[0] == -1
