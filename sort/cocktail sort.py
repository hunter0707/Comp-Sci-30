import random

n = '9 8 7 6 5 4 3 2 1 0'.split()
n = [int(x) for x in n]
#n = [1,2,3,4,5,6,7,8,9,0]
#random.shuffle(n)

def cocktailSort(n):
        r = 0
        hl = round(len(n)/2) #half length
        l = len(n)
        
        for i in range(hl):
            unsorted = False       
            for a in range(i, l-1): #forward, goes from i to length, 
                if n[a] > n[a+1]: #if current greater then next
                    n[a], n[a+1] = n[a+1], n[a] #swap places
                    unsorted = True
                    r += 1
            for b in range(l-1, i, -1): #backwards, goes from length - 1 to i
                if n[b] < n[b-1]:
                    n[b], n[b-1] = n[b-1], n[b]
                    unsorted = True
                    r += 1
            l -= 1 #i increases while l decreases, thereby only running through the unsorted parts of the list
            if unsorted == False: #no changes
                return r

print(cocktailSort(n))