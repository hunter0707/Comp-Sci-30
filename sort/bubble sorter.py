import random
import time

n = input("enter numbers separated by space: ").split()
for i in range(0,1500,1):
        n.append(i)
random.shuffle(n)
print(n)

start_time = time.time()

def bubbleSort(n):
        print(n)
        unsorted = True
        while unsorted:
                #print(n, 'run')
                unsorted = False
                for a in range(len(n) - 1):
                        if int(n[a]) > int(n[a+1]): #if current greater then next
                                n[a], n[a+1] = n[a+1], n[a] #swap places
                                unsorted = True #if change is made, list isn't sorted
        return n
   
print(bubbleSort(n), 'finished')
print(time.time() - start_time)
