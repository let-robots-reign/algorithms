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


stack = []
for brace in input():
    if brace in "([{":
        push(stack, brace)
    else:
        if is_empty(stack):
            print("NO")
            break
        if not (pop(stack) + brace in ["()", "[]", "{}"]):
            print("NO")
            break
else:
    if is_empty(stack):
        print("YES")
    else:
        print("NO")
