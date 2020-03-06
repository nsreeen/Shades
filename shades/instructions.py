
def reset_counter(state):
    state.counter = 1
    return state

def inc_counter(state):
    state.counter += 1
    return state

def push(state):
    state.stack.append(state.counter)
    state = reset_counter(state)
    return state

def pop(state):
    state.stack.pop()
    return state

def add(state):
    a = state.stack.pop()
    b = state.stack.pop()
    state.stack.append(a + b)
    return state

def multiply(state):
    a = state.stack.pop()
    b = state.stack.pop()
    state.stack.append(a * b)
    return state

def duplicate(state):
    state.stack.append(state.stack[-1])
    return state

def number_out(state):
    print(str(state.stack[-1]))
    return state

def char_out(state):
    print(chr(state.stack[-1]))
    return state

def toggle_star(state):
    state.star = not state.star
    return state

def on_black(state):
    state = toggle_star(state)
    state = reset_counter(state)
    return state