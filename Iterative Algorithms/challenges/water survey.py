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
    land = land.replace('|',' ') #replace all | with spaces so it can be split
    land = land.split() #convert the array into a list of numbers
    land = [int(i) for i in land] #convert all numbers in list into integers
    print('all land: ', land)
    water = []
    volume = 0
    for i in land:
        if land[i] > 0: #if current square is greater then 0 then it contains water
            water.append(land[i]) 
    print('all water: ', water)
    for i in water:
        volume += water[i] #sum of all squares with water
    return('total volume of water is ' + str(volume) + ' kiloliters.') #m^3 = kL

land = makeLand()
print(land)
print(countWater(land))

