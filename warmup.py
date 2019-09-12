import random

def randomList(u):
    a = []
    length = random.randint(5,30)
    for i in range(length):
        b = random.randint(0,1000)
        if u:
            if b not in a:
                a.append(b)
        else:
            a.append(b)
    return(a)


item = 'seven'

while True:
    a = input("enter one of the following commands: create, fill (with random values), sort (from smallest to largest), scramble (shuffle list), print, search, count, unique (fill list with unique values), quit: ")

    if a == "create":
        l = []
    elif a == "fill":
        l = randomList(False)
        print(l)
    if l in globals():
        if l != []:
            if a == "sort":
                l = l.sort()
                print(l)
            elif a == "scramble":
                random.shuffle(l)
                print(l)
            elif a == "print":
                print(l)
            elif a == "search":
                while item not in l:
                    item = input("what number would you like to search for?: ")
                    if item not in l:
                        input("item is not in the list, try again.")
                print(item + ' is in position ' + l.index(item))
            elif a == "count":
                while item not in l:
                    item = input("what number would you like to count?: ")
                    if item not in l:
                        input("item is not in the list, try again.")
                print(item + ' is in the list ' + list.count(item) + ' times.')

        
        
