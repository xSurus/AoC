aim = 0
horizontal = 0
depth = 0
def words(fileobj):
    for line in fileobj:
        for word in line.split():
            yield word
with open('input2.txt') as my_file:
    wordgen = words(my_file)
    for word in wordgen:
        if word == 'forward':
            val = int(next(wordgen, None))
            horizontal += val
            depth += aim * val
        if (word == 'down'):
            aim += int(next(wordgen, None))
        if (word == 'up'):
            aim -= int(next(wordgen, None))
print(horizontal*depth)
