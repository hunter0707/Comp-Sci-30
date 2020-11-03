def drawTriangles(l):
    for i in range(l):
        sf = ' '*(l - 1 - i) #number of spaces before first * is final - (elapsed + 1)
        t = '*' + ' '*(i*2-1) + '*' #walls are * and middle is (i*2-1) spaces
        if i == 0 or i == l - 1: #first and final are all *
            print(sf + ('* '*(i+1))) #front spacing and then all *
        else: #all else is * spaces *
            print(sf + t) #front spacing + t
play = True
 
while play:
    l = 1
    while l < 2 or l > 25: 
        l = input('Enter a triangle height from 2 to 25 or 0 to quit: ')
        if l == '': #you can't int '' so i had to do this
            l = 1
        else:
            l = int(l)
        if l == 0:
            print('thanks for playing')
            play = False
            break
    drawTriangles(l)