import random

#n = input("enter numbers separated by space: ").split()
n = [6,5,3,1,8,7,2,4]
print(n)

def mergesort(n,x,y):
    #def merge(a,b):
    print(n)
    if len(n) > 1:
        a = n[:len(n)//2]
        b = n[len(n)-len(n)//2:]
    return n

print(mergesort(n,[],[]))