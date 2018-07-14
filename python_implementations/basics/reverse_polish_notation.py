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
s = input().split()
for char in s:
    if "0" <= char <= "9":
        push(stack, int(char))
    else:
        a = pop(stack)
        b = pop(stack)
        if char == "+":
            push(stack, b + a)
        elif char == "-":
            push(stack, b - a)
        elif char == "*":
            push(stack, b * a)

print(pop(stack))
