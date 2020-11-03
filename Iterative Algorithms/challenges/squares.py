def drawSquare(l):
    for i in range(l):
        if i == 0 or i == l - 1:
            print(' * '*l) #first or last, print only *
        else:
            print(' * ' + ('   ' * (l-2)) + ' *') #everything in between, print * on 2 sides and spaces in the middle
        
play = True
 
while play:
    l = 1
    while l < 2 or l > 50: 
        l = input('Enter a square side size from 2 to 50 or 0 to quit: ')
        if l == '': #you can't int '' so i had to do this
            l = 1
        else:
            l = int(l)
        if l == 0:
            print('thanks for playing')
            play = False
            break
    drawSquare(l)