import random

def randomList(u):
    a = []
    length = int(input('how long do you want your list?: '))
    for bruh in range(length - 1): #within length - 1
        b = random.randint(1,length) #random integer between 1 and length
        if u: #if unique
            while b in a: #generate new int if current already exists
                b = random.randint(0,length)
            a.append(b)
        else:
            a.append(b)
    return(a)

l = []
item = 'seven'

while True:
    a = input("enter one of the following commands: create, fill (with random values), sort (from smallest to largest), scramble (shuffle list), print, search, count, unique (fill list with unique values), quit: ")

    if a == "create":
        l = []
        print('empty list has been created')
    elif a == "fill":
        l = randomList(False)
        print(l)
    elif a == "unique":
        l = randomList(True)
        print(l)
    elif a == "quit":
        print('program has quit')
        break
    elif l != []:
        if a == "sort":
            l = sorted(l)
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
            print(item + ' is in index ' + l.index(item)) #index of item
        elif a == "count":
            while item not in l:
                item = input("what number would you like to count?: ")
                if item not in l:
                    input("item is not in the list, try again.")
            print(item + ' is in the list ' + list.count(item) + ' times.') #number of occurences of item
    else:
        print("your input isn't valid, try again.")

        
        
