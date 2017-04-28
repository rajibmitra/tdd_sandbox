def fib(input_value):
    n = int(input_value)
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
