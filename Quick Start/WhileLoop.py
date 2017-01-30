#!/usr/bin/python3.5
# Simple Fibonacci series
# Sum of 2 elements defines next set

a, b, n = 0, 1, 1
while n <= 100:
    print('Iteration {}: {}'.format(n, b))
    a, b = b, a + b
    n += 1
