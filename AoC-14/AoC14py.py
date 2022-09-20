import math
data = [line.rstrip().split() for line in open('input.txt').readlines()]
start = list(data[0])
data.remove(data[0])
data.remove(data[0])
data = [[line[0],line[2]] for line in data]
print(data)
funct = {}
counter = {}
for i in data:
    funct[i[0]] = i[1]
    counter[i[0]] = 0
for i in range(len(start)-1):
    counter[start[i] + start[i+1]] += 1
    
print(counter)
for _ in range(40):
    newC = dict.fromkeys(counter, 0)
    for i in counter:
        if counter[i] != 0:
            newC[i[0] + funct[i]] += counter[i]
            newC[funct[i] + i[1]] += counter[i]
    counter = newC
    #print(counter)
sum = {}
for i in counter:
    #print("asdf")
    if i[0] not in sum:
        sum[i[0]] = 0
    sum[i[0]] += counter[i]
    if i[1] not in sum:
        sum[i[1]] = 0
    sum[i[1]] += counter[i]
print(math.ceil(max(sum.values())/2) - math.ceil(min(sum.values())/2))