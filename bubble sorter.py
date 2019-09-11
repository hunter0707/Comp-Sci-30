n = input("enter numbers separated by space: ").split()

def bubbleSort(n, b):
        print("run")
        print(n)
        a = b
        while a < (len(n) - 1):
                if int(n[a]) > int(n[a+1]):
                        n[a], n[a+1] = n[a+1], n[a]
                        a += 1
                        print(n)
                else:   
                        print(n)
                        return n
        return n

a = 0

def check(n):
       

while check(n) == False:
        bubbleSort(n,a)
        a += 1
        if a == len(n):
                a = 0
