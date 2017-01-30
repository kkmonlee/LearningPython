def is_prime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


def primes(n=1):
    while True:
        if is_prime(n): yield n
        n += 1
# Yield is like return. It returns a value only if is_prime(n) returns true
# Yield keeps returning values and does not stop the function like a
# typical boolean, int, double, etc. function would stop after a return.

for n in primes():
    if n > 100: break
    print(n)
