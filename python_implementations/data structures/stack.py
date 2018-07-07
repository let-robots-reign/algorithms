def push(stack, x):
    stack.append(x)


def pop(stack):
    return stack.pop()


def top(stack):
    return stack[-1]


def is_empty(stack):
    return len(stack) == 0


def clear(stack):
    stack[:] = []
