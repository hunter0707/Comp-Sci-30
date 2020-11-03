import random, time

n = input("enter numbers separated by space: ").split()
n = [int(x) for x in n]
n = [6,5,3,1,8,7,2,4]
print(n)

def mergesort(n):
    #print('input:', n)
    def merge(left,right): #sorts and merges left and right
        #print('left and right:',left,right)
        r = []

        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]: #first item of left is removed and added to result list if first left is smaller than first right
                r.append(left[0]) 
                del left[0]
            else: #same for right
                r.append(right[0])
                del right[0]

        if len(left) == 0:
            r.extend(right) #all items in individual sub lists are already sorted and the items in the main list are smaller than these so they can be added to result list
        else:
            r.extend(left) #if left isn't empty then the right list is empty because of the while loops end condition
        #print('sorted sublist: ', r)
        return r
        
    if len(n) <= 1: #lists split until they reach a length of 1 which means that they are already sorted
        return n #first return of n is the left most
    
    mid = len(n) // 2
    left = mergesort(n[:mid]) #left half of n is sorted
    right = mergesort(n[mid:]) #right half of n is sorted

    #once last of left and right are sorted, they are merged together
    
    return merge(left,right) #left and right are merged and sorted together

print(mergesort(n))