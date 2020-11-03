import random
import sys
import time

class elevator:
    def __init__(self,minFloor,maxFloor,current):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.current = current
        self.serviceMode = False
    def moveFloor(self,destination):
        if self.serviceMode:
            print('SERVICE MODE')
        elif destination in range(self.minFloor,self.maxFloor+1) and destination != self.current: #between min and max floor, inclusive
            self.current = destination #move from current to destination
            print('The elevator moved to floor ' + str(destination) + '.')
    def __str__(self):
        status = 'The elevator is '
        if self.serviceMode:
            status += 'in service mode ' #'in service mode' is in between 
        status += 'on floor ' + str(self.current) + '.'
        return status
    def SMToggle(self): #service mode toggle
        if self.serviceMode:
            self.serviceMode = False
        else:  
            self.serviceMode = True

class smartElevator(elevator):
    def __init__(self,minFloor,maxFloor,current):
        elevator.__init__(self,minFloor,maxFloor,current)
    def moveFloor(self,destination):
        if self.serviceMode:
            print('SERVICE MODE')
        elif destination in range(self.minFloor,self.maxFloor+1):
            u = -1 #moving down
            if destination > self.current:
                u = 1 #moving up
            for f in range(self.current+u,destination+u,u): #if moving up, starts at current + 1 and ends at destination because range not inclusive of stop, vice versa for moving down
                time.sleep(0.1) #0.5s between each floor being printed
                sys.stdout.write(str(f) + ' ') #one floor at a time
                sys.stdout.flush()
            print('') #end flush
            self.current = destination

def setFloors():
    minFloor = input('minimum floor: ')
    try:
        minFloor = int(minFloor)
    except:
        minFloor = 1 #not convertable to int, set min floor to 1
    maxFloor = input('maximum floor: ')
    try:
        maxFloor = int(maxFloor)
    except:
        maxFloor = 20 #max is 20 if not int
    if maxFloor < minFloor:
            maxFloor = minFloor + 10 #add 10 to min for max if min > max
    current = input('current floor: ')
    try:
        current = int(current)
    except:
        current = minFloor #not number, set current to min
    if current not in range(minFloor,maxFloor + 1): #min floor if not in range
        current = minFloor
    fset = {'minFloor':minFloor,'maxFloor':maxFloor,'start':current}
    return(fset) #returns as dictionary

def play(e):
    play = True
    while play:
        command = input('choose command: 1 to move floor, 2 to print the current status, and 3 to turn service mode on or off (4 to stop): ')
        if command == '4':
            play = False #stop playing
        if command == '1':
            destination = input('move to floor: ')
            try:
                destination = int(destination)
            except:
                destination = e.maxFloor + 1 #out of range, prints nothing
            e.moveFloor(destination)
        elif command == '2':
            print(e)
        elif command == '3':
            e.SMToggle()

minFloor = 1
maxFloor = 20 #defaults

print('')
print('Elevator')
print('')
e1floors = setFloors()
e1 = elevator(e1floors['minFloor'],e1floors['maxFloor'],e1floors['start'])
play(e1)

print('')
print('Smart Elevator')
print('')
e2floors = setFloors()
e2 = smartElevator(e2floors['minFloor'],e2floors['maxFloor'],e2floors['start'])
play(e2)