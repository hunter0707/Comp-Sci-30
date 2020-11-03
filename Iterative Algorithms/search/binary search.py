import random

n = []

for i in range(random.randint(50,100)):
    r = random.randint(1,250)
    if r not in n:
        n.append(r)

random.shuffle(n)

for i in range(len(n)): #while in range of len of list
        current = int(n[i]) #starts at 0th then goes up
        for b in range(i,-1,-1): #counts from i to 0, steps is -1 therefore counting down
            if current < int(n[b]): #if less then n[b]
                n.insert(b,current)      
                del n[b+2]
print(n)

f = int(input("what number would you like to search for?: "))     

def binarySearch(n,f):
    notfound = True
    end = len(n) #len - 1 is index of last term
    start = 0 #index of first item
    while notfound:
        l = round((start + end) / 2) #average of start and end is middle
        print('from', start, 'to', end, '| index =', l, '| n[l] =', n[l])
        if f == n[l]:
            notfound = False
        elif f > n[l]:
            start = l #new start at l
        elif f < n[l]:
            end = l #new ending at l
        if end - start == 1 and f != n[l]: #if start and end is within 1 of each other and current index is not f
            return(str(f) + ' not in list')
    return(str(f) + ' found at index ' + str(l))

print(binarySearch(n,f))