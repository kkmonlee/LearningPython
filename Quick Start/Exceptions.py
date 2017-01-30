fh = open('xlines.txt')
try:
    for line in fh.readlines():
        print(line)
except IOError as e:
    print("something bad happened", e)
print("after badness")