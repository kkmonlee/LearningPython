# Read lines from the file
fh = open('lines.txt')

# For loops works with iterator.
# Iterator is an object where each time you call it, it gives you the next object
for line in fh.readlines():
    print(line, end='')
# Here, readlines() is an iterator. Each time readlines() is called it will
# put the next value in the 'line' variable.
