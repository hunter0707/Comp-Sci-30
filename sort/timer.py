import random
import time

def bubbleSort(n):
        #print(n)
        unsorted = True
        while unsorted:
                #print(n, 'run')
                unsorted = False
                for a in range(len(n) - 1):
                        if int(n[a]) > int(n[a+1]): #if current greater then next
                                n[a], n[a+1] = n[a+1], n[a] #swap places
                                unsorted = True #if change is made, list isn't sorted
        return n

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

def insertionSort(n):
    #print(n)
    for i in range(len(n)): #while in range of len of list
        current = int(n[i]) #starts at 0th then goes up
        for b in range(i,-1,-1): #counts from i to 0, steps is -1 therefore counting down
            if current < int(n[b]): #if less then n[b]
                n.insert(b,current)      
                del n[b+2]
        #print(n, 'run', i+1)
    return n

def selectionSort(n):
    #print(n)
    mindex = 0
    for i in range(len(n)):
        #print(n, 'run', i+1)
        currentMin = int(n[i]) #current minimum is i, +1 per cycle, starts at 0
        for b in range(i, len(n)): #only runs from i to length instead of 0 to length
            if int(n[b]) <= currentMin: #if current number is less then or equal to currentMin
                currentMin = int(n[b]) #currentMin is now current number
                mindex = b #minimum index is b
        n[i], n[mindex] = n[mindex], n[i] #swap places
    return n

n = []
lists = 5
ints = 2000
for i in range(0,ints,1):
        n.append(i)
random.shuffle(n)

sorters = [bubbleSort, cocktailSort, gnomeSort, insertionSort, selectionSort]

print(lists, 'lists... each with', ints, 'integers... which sorting algorithm comes out top?')

for i in range(len(sorters)):
    tt = 0
    longest = 0
    shortest = 10
    for a in range(lists):
        random.shuffle(n) #reshuffle list
        time_start = time.time() #begin timer
        sorters[i](n) #runs sorter
        time_taken = time.time() - time_start #end timer
        if time_taken > longest: #new longest time
            longest = time_taken
        elif time_taken < shortest: #new shortest time
            shortest = time_taken
        tt += time_taken #total time taken
    at = tt/lists #average time
    print(sorters[i],"total time = ", tt, ", average time = ", at, ', longest time = ', longest, ', shortest time = ', shortest)