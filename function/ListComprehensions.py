list = [x * x for x in range(1, 10, 2)]
print list

def fib(max_value):
    n, a, b = 0, 0, 1
    while n < max_value:
        yield b
        a, b = b, a + b
        n = n + 1

fib_num = fib(6)
print fib_num