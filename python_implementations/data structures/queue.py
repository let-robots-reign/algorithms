def enqueue(elem):
    global queue, head, tail
    tail += 1
    queue[tail] = elem

    # if the queue contains too many empty cells
    if head * 2 > len(queue):
        queue = queue[head:]
        head = 0


def dequeue():
    global head
    elem = queue[head]
    head += 1
    return elem


def front():
    return queue[head]


def size():
    return head - tail + 1


def is_empty():
    return (head - tail + 1) == 0


n = 50  # for instance, the queue contains 50 elements
queue = [0] * n
head = 0
tail = -1
