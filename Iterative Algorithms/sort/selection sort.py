n = input("enter numbers separated by space: ").split()

def selectionSort(n):
    print(n)
    mindex = 0
    for i in range(len(n)):
        print(n, 'run', i+1)
        currentMin = int(n[i]) #current minimum is i, +1 per cycle, starts at 0
        for b in range(i, len(n)): #only runs from i to length instead of 0 to length
            if int(n[b]) <= currentMin: #if current number is less then or equal to currentMin
                currentMin = int(n[b]) #currentMin is now current number
                mindex = b #minimum index is b
        n[i], n[mindex] = n[mindex], n[i] #swap places
    return n

print(selectionSort(n), 'finished')