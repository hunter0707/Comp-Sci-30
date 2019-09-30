n = '10 9 8 7 6 5 4 3 2 1'.split()
n = [int(x) for x in n]

def gnomeSort(n):
    r = 0
    a = 0
    unsorted = True
    while unsorted:
        r += 1
        #print(n, a, r)
        if a > 0 and a < len(n) and n[a] < n[a-1]:
            n[a], n[a-1] = n[a-1], n[a]
            if a > 0:
                a -= 1
        else:
            a += 1
        if a == len(n):
            unsorted = False
    return r

print(gnomeSort(n))