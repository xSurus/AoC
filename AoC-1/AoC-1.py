with open('input1 .txt') as my_file:
    lines = my_file.readlines()
counter = 0
for i in range(1,len(lines)):
    if int(lines[i-1]) < int(ines[i]):
        counter+=1
print(counter)
"""
array = []
pointer = 0;
with open('input1.txt') as my_file:
    lines = my_file.readlines()
sum = []
for i in range(len(lines)-2):
    sum.append(int(lines[i]) + int(lines[i+1]) + int(lines[i+2]))
counter = 0
for i in range(1,len(sum)):
    # print(int(sum[i]))
    if int(sum[i-1]) < int(sum[i]):
        counter+=1
print(counter)"""