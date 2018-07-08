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
s = input()
for brace in s:
    if brace in "([{":
        push(stack, brace)
    elif is_empty(stack):
        print("NO")
        break
    elif brace == ")":
        if top(stack) != "(":
            print("NO")
            break
        else:
            pop(stack)
    elif brace == "]":
        if top(stack) != "[":
            print("NO")
            break
        else:
            pop(stack)
    elif brace == "}":
        if top(stack) != "{":
            print("NO")
            break
        else:
            pop(stack)
else:
    if is_empty(stack):
        print("YES")
    else:
        print("NO")
