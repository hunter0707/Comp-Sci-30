import random
import time
import sys

class spaceship:
    def __init__(self,name):
        self.name = name
        self.location = 0
        self.fuel = 100
        self.destination = 628743036 #distance to jupiter i.e. destination
    def fly(self):
        self.fuel -= 1
        self.location += 10000000
    def __str__(self):
        if self.location > self.destination:
            self.location = self.destination #if farther, make same
        return 'The spaceship ' + self.name + ' is ' + str(self.location) + ' km away from Earth and has ' + str(self.fuel) + '% of its fuel remaining. ' 

class warpship(spaceship): #inherits spaceship class
    def __init__(self,name):
        spaceship.__init__(self,name)
        self.warps = 5
    def fly(self):
        if self.warps > 0:
            self.location += random.randint(0,60000000) #random additional distance
            self.fuel -= 3
            self.warps -= 1
        else:
            spaceship.fly(self)
    def __str__(self):
        status = spaceship.__str__(self) 
        status += str(self.warps) + ' warp(s) remaining.'
        return status 
        
def launch(ship):
    notarrived = True
    time.sleep(1)
    def print1(status,sleeptime): #print 1 char at a time
        for s in status:
            sys.stdout.write(s) #writes current letter
            sys.stdout.flush()
            time.sleep(sleeptime) #time between each letter
    for i in range(8,-1,-1):
        tframe = 0.7 #time to print string
        if i == 0:
            lstatus = 'Blast off!'
        elif i == 8:
            lstatus = ship.name + ': '
            tframe = 1.5
        elif i == 7:
            time.sleep(0.5) #wait half second between ship name and this
            lstatus = 'Launch Commencing...'
            tframe = 2
        elif i == 6:
            lstatus = '10.. 9.. 8... 7... 6....' 
            tframe = 5 #5 second count down
        else:
            lstatus = str(i) + '.'*(9-i) #period after each, increasing over time
        sleeptime = tframe/(len(lstatus)) #time between each letter
        print1(lstatus,sleeptime)
        if i != 8:
            print('') #new line if not 8
        time.sleep(0.3) #0.2 seconds between each count
    time.sleep(0.25)
    print(' .......')
    time.sleep(0.25)
    while notarrived:
        time.sleep(0.1) #0.1 second between each print
        ship.fly()
        print(ship)
        if ship.location == ship.destination:
            notarrived = False #loop break
            time.sleep(0.5)   
            print1(ship.name + ' has arrived at Jupiter!',0.07)
            time.sleep(1)
    print('') #break flush
    print('') #line skip

launch(spaceship('Patriot I'))
launch(warpship('Patriot II'))