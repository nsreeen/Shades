def toggle_star(state):
    state.star = not state.star
    return state

def reset_counter(state):
    state.counter = 1
    return state

def on_black(state):
    state = toggle_star(state)
    state = reset_counter(state)
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
    top = state.stack.pop()
    second = state.stack.pop()
    state.stack.append(second + top)
    return state

def mul(state):
    top = state.stack.pop()
    second = state.stack.pop()
    state.stack.append(second * top)
    return state

def sub(state):
    top = state.stack.pop()
    second = state.stack.pop()
    state.stack.append(second - top)
    return state

def div(state):
    top = state.stack.pop()
    second = state.stack.pop()
    state.stack.append(second / top)
    return state

def mod(state):
    top = state.stack.pop()
    second = state.stack.pop()
    state.stack.append(second % top)
    return state

def dup(state):
    state.stack.append(state.stack[-1])
    return state

def not_(state):
    state.stack[-1] = state.stack[-1] * -1
    return state

def greq(state):
    top = state.stack.pop()
    second = state.stack.pop()
    result = 1 if top >= second else -1
    state.stack.append(result)
    return state

def number_out(state):
    print(str(state.stack[-1]))
    return state

def char_out(state):
    print(chr(state.stack[-1]))
    return state
