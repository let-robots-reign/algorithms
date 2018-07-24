def push(x):
    stack.append(x)


def pop():
    return stack.pop()


def top():
    return stack[-1]


def size():
    return len(stack)


def is_empty():
    return len(stack) == 0


def clear():
    stack[:] = []


stack = []
