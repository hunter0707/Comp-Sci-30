import sys
import time
import random

class elevator:
    def __init__(self,floor,inServiceMode):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.inServiceMode = inServiceMode
        self.floor = 1
    def create(self):
        self.floor = self.minFloor
        self.inServiceMode = True
    def statusCheck(self):
        status = 'The elevator is on floor ' + str(self.floor)
        if self.inServiceMode:
            status += 'and it is in service mode.'
        print(status)
    def goToFloor(self,destination):
        if destination >= self.minFloor and destination <= self.maxFloor and not self.inServiceMode:
            print('The elevator moved to floor ' + str(destination) + '.')
        elif self.inServiceMode:
            print('SERVICE MODE')
    def serviceMode(self,on):
        if on:
            self.inServiceMode = True
        else:
            self.inServiceMode = False
    def setFloors(self,minFloor,maxFloor)

class smartElevator:
    def __init__(self,minFloor,maxFloor):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.inServiceMode = True
        self.floor = 1
    def statusCheck(self):
        status = 'The elevator is on floor ' + str(self.floor)
        if self.inServiceMode:
            status += 'and it is in service mode.'
        print(status)
    def goToFloor(self,destination):
        if destination >= self.minFloor and destination <= self.maxFloor and not self.inServiceMode:
            for i in (self.floor + 1,destination + 1,1):
                sys.stdout.write(str(i) + ' ')
                sys.stdout.flush()
                time.sleep(0.2)
        elif self.inServiceMode:
            print('SERVICE MODE')
    def serviceMode(self,on):
        if on:
            self.inServiceMode = True
        else:
            self.inServiceMode = False

minFloor = 1
maxFloor = 20

elevator1 = elevator(minFloor,maxFloor)
elevator2 = smartElevator(minFloor,maxFloor)

def runElevator(elevator):
    minFloor = int(input('minimum floor: '))
    maxFloor = int(input('maximum floor: '))
    functions = [elevator.statusCheck(),elevator.goToFloor(),elevator.serviceMode()]
    for i in range(random.randint(10,20)):
        task = functions[random.randint(0,2)]


