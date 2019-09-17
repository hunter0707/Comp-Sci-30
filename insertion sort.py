n = input("enter numbers separated by space: ").split()

def insertionSort(n):
    print(n)
    for i in range(1, len(n)):
        print('run')
        print(i, 'i')
        current = int(n[i-1]) #starts at 0th then goes up
        print(current, 'current')
        for b in range(1,i+1):
            print('current and n[b]', current, n[b])
            if int(current) >= int(n[b]) and int(current) <= int(n[b-1]):
                print('yes')
                n.insert(i-1,n[b])
                del n[b+1]
            print(n)
    return n

print(insertionSort(n), 'finished')