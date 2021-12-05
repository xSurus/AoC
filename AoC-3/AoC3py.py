aim = 0
horizontal = 0
depth = 0

def split(word):
    return [char for char in word]

with open('input.txt') as my_file:
    # bits = [0,0,0,0,0]
    # bits = [0,0,0,0,0,0,0,0,0,0,0,0]
    b = []
    for line in my_file:
        a = split(line.rstrip("\n"))
        b.append(a)
        """counter = 0
        for bit in a:
            if (bit == '1'): bits[counter] += 1;
            else: bits[counter] -= 1;
            counter += 1
    bitsMA = []
    bitsMI = []
    for bitss in bits:
        if bitss > 0: bitsMA.append("1"); bitsMI.append("0")
        elif bitss == 0: bitsMA.append("1"); bitsMI.append("1")
        else: bitsMA.append("0"); bitsMI.append("1")
    print(bitsMA, "Majority bits")"""
    # b.remove([])
    newb = b
    result = 1;
    for i in range(12):
        c = 0
        for bi in newb:
            if bi[i] == "1": c+=1
            else: c-=1
        if c >= 0: c = 1
        else: c = 0
        newb = [elem for elem in newb if elem[i] == str(c)]
        if len(newb) == 1: result *= int(''.join(newb[0]),2)
    newwb = b
    for i in range(12):
        c = 0
        for bi in newwb:
            # print("hi   ")
            if bi[i] == "1": c+=1
            else: c-=1
        if c >= 0: c = 0
        else: c = 1
        # print(c)
        newwb = [elem for elem in newwb if elem[i] == str(c)]
        if len(newwb) == 1: result *= int(''.join(newwb[0]),2); print(newwb)
    print(result)