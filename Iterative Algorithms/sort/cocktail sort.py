n = '4 -1 25 13 19 -5 0 21 19 1'.split()
n = [int(x) for x in n]

def cocktailSort(n):
    r = 0 #goes up per swap
    l = len(n)
    i = 0 #goes up per while loop
    unsorted = True
    while unsorted:
        unsorted = False #stays false unless sorted
        for a in range(i, l-1): #forward, goes from i to length, 
            if n[a] > n[a+1]: #if current greater then next
                n[a], n[a+1] = n[a+1], n[a] #swap places
                unsorted = True
                r += 1
        for b in range(l-1-i, i, -1): #backwards, goes from length - 1 to i
            if n[b] < n[b-1]: #if current less then prior
                n[b], n[b-1] = n[b-1], n[b] #place swap
                unsorted = True
                r += 1
        i += 1
        if unsorted == False: #no changes, i.e. sorted
            return r
    return r
   
print(cocktailSort(n))