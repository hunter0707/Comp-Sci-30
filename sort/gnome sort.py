n = '4 -1 25 13 19 -5 0 21 19 1'.split()
n = [int(x) for x in n]

def gnomeSort(n):
    r = 0
    for i in range(len(n)):
        print(i)
        for a in range(i,-1,-1):
            print(a,'a')
            r += 1
            if n[a] > n[a-1]:
                n[a], n[a-1] = n[a-1], n[a]
                r += 1
    print(n)
    return r

print(gnomeSort(n))