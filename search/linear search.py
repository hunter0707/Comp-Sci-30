import random

n = []
for i in range(random.randint(5,35)):
    n.append(random.randint(0,10))

def linearSearch(n,f):
    indicies = []
    for i in range(len(n)):
        if f == n[i]:
            indicies.append(i) #add index found at to list
    if len(indicies) == 0:
        print(str(f) + ' not found') #none found because none added to list
    else:
        print(str(f) + ' found at index ' + str(indicies)[1:-1]) #removes square brackets

print(n)

f = int(input("what number would you like to search for?: "))

linearSearch(n,f)