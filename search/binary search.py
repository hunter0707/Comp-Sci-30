n = []
for i in range(random.randint(100,200)):
    n.append(random.randint(1, 300))

print(n)

f = int(input("what number would you like to search for?: "))

def binarySearch(n,f):
    l = len(n)
    for i in range(l): #while in range of len of list
        current = int(n[i]) #starts at 0th then goes up
        for b in range(i,-1,-1): #counts from i to 0, steps is -1 therefore counting down
            if current < int(n[b]): #if less then n[b]
                n.insert(b,current)      
                del n[b+2]
    for i in range(l):
        l = l / 2
        if f = n[l]:
            
            
