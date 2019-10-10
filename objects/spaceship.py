class spaceship:
    def __init__(self,name,location,fuel,warp):
        self.name = name
        self.location = location
        self.fuel = fuel
        self.warp = warp
    def printShip(self,iswarp):
        print('The spaceship ' + self.name + ' is ' + self.location + ' km away from Earth and has ' + self.fuel + '%% of its fuel remaining')


name = input('name of spaceship: ')
location = 628743036
fuel = 100
warp = 5
iswarp = False

ship = spaceship(name,location,fuel,warp)
    