inp = [line.split() for line in open('input.txt').readlines()]
for i in inp:
    c = [0] * 6
    r = 
    for j in range(0,11):
        for k in i[j]:
            match k:
                case 'a': c[0] += 1
                case 'b': c[1] += 1
                case 'c': c[2] += 1
                case 'd': c[3] += 1
                case 'e': c[4] += 1
                case 'f': c[5] += 1
                case 'g': c[6] += 1