n = input("enter numbers separated by space: ").split()

def bubbleSort(n):
        print(n)
        a = 0
        while a < len(n) - 1:
                print("run") #prints per function run i.e. per cycle
                for a in range(len(n) - 1):
                        if int(n[a]) > int(n[a+1]): #if current greater then next
                                n[a], n[a+1] = n[a+1], n[a] #swap places
                                print(n)
                        a += 1
                for i in range(len(n) - 1):
                        if int(n[i]) > int(n[i+1]): #check if all values are less or equal to next value
                                a = 0
        print('finished')
        return n
        
bubbleSort(n)