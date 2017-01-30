#!/usr/bin/python3.5

a, b = 6, 1

if a < b:
    # Blocks of code are called suites
    # 4 spaces/a tab is not needed. You can make Python work with 1 space of
    # indentation
    print('a ({}) is less than b ({})'.format(a, b))
else:
    print('a ({}) is not less than b ({})'.format(a,  b))

# Conditional expression
# Equivalent to print(a < b ? "foo" : "bar")
print("foo" if a < b else "bar")
