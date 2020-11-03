n = input("enter numbers separated by space: ").split()
n = [int(x) for x in n]

def insertionSort(n):
    print(n)
    for i in range(len(n)): #while in range of len of list
        current = int(n[i]) #starts at 0th then goes up
        for b in range(i,-1,-1): #counts from i to 0, steps is -1 therefore counting down
            if current < int(n[b]): #if less then n[b]
                n.insert(b,current)      
                del n[b+2]
        print(n, 'run', i+1)
    return n

print(insertionSort(n), 'finished')   