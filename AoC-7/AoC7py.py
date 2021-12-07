inp = [line.strip().split(',') for line in open('input.txt').readlines()]
inp = inp[0]
print(inp)
maxnum = 0
for i in inp:
    maxnum = max(maxnum,int(i))
lst = [0] * maxnum
for i in inp:
    for j in range(len(lst)):
        if (j == 5): print(abs(int(i)-j), (pow(abs(int(i)-j),2)+ abs(int(i)-j))/2)
        lst[j] += (pow(abs(int(i)-j),2) + abs(int(i)-j))/2
print(lst, len(lst))
"""for i in range(len(lst)):
    lst[j] = lst[j]/len(inp)"""
print(min(lst))