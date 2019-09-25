import random

def makeLand():
    l = random.randint(3,22) #length
    w = random.randint(3,22) #width
    line = ''
    land = ''
    for i in range(l):
        line = '' 
        for i in range(w):
            d = random.randint(-10,10)
            if d == -10: #no space if -10, 1 space if 2 char, 2 space if 1 char, each is 3 char long
                s = ''
            elif d < 0 or d == 10:
                s = ' '
            elif d >= 0 and d != 10:
                s = '  '
            newSeg = '|' + s + str(d)
            if i == w-1:
                newSeg += '|' # use of | indicates new square
            line += newSeg 
        land += '\n' + line #new line
    return land

def countWater(land):
    land = land.replace('|',' ')
    land = land.split()
    land = [int(i) for i in land]
    print('all land: ', land)
    water = []
    for i in land:
        if land[i] > 0:
            water.append(land[i])
    print('all water: ', water)

land = makeLand()
print(land)
countWater(land)

