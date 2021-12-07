with open('input.txt') as my_file:
    firstline = my_file.readline()
    nums = firstline.rstrip("\n").split(',')
    nums = [int(x) for x in nums]
    groups = [0,0,0,0,0,0,0,0,0]
    for i in nums:
        groups[i] += 1
    for i in range(256):
        #print(groups)
        newF = groups[0]
        for j in range(len(groups)-1):
            groups[j] = groups[j+1]
        groups[8] = newF
        groups[6] += newF
        #print(nums)
        #print(groups)
    sum = 0
    #print(groups)
    for i in groups:
        sum += i
    print(sum)