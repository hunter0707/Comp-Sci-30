import random
n = '4 -1 25 13 19 -5 0 21 19 1'.split()
n = [random.randint(0,100) for x in range(20)]
n = [int(x) for x in n]

def gnomeSort(n):
    r = 0 #run
    a = 0 #position in list
    unsorted = True
    while unsorted:
        r += 1 #+ 1 per run
        #print(n,r)
        if a > 0 and a < len(n) and n[a] < n[a-1]:
            n[a], n[a-1] = n[a-1], n[a]
            if a > 0: #a does not become negative
                a -= 1 #keep going down list if its bigger
        else:
            a += 1 #goes up to next
        if a == len(n): #gone to end of list i.e. finished sorting
            unsorted = False
    return r

print(gnomeSort(n))