class coin:
    def __init__(self,name,d,material,value):
        self.r = d/2
        self.name = name
        self.pi = 3.1415926535897932384626433832795
        self.material = material
        self.value = value
    def getCircumference(self):
        return str(2*self.pi*self.r) #2 pi r
    def getArea(self):
        return str(self.pi*(self.r**2)) #pi r squared
    def __str__(self):
        string = '- The surface area of one side of a ' + self.name + ' is ' + self.getArea() + ' mm². \n' #new line each time
        string += '- A ' + self.name + "'s circumference is " + self.getCircumference() + ' mm. \n'
        string += '- The ' + self.name + ' is made of ' + self.material + '. It has a value of ' + str(self.value) + ' cents.'
        return string

def reqdcoins(target,coins):
    lim = 0
    i = 0
    reqd = []
    while lim < target and i < len(coins): 
        if coins[i].value + lim <= target: #goes from largest to smallest denom
            lim += coins[i].value #lim approaches target
            reqd.append(coins[i].name) #reqd coin added to reqd list
        else:
            i += 1 #go on to next coin, which is smaller
    return reqd

def countcoins(ucoins,coins):
    ulist = []
    counted = ''
    for i in range(len(coins)):
        uname = coins[i].name   
        uses = ucoins.count(uname) #number of occurences of current coin
        if uses > 0:
            if uses > 1: #plural if > 1
                uname += 's'
                if uname == 'pennys': #pennies if it's pennys
                    uname = 'pennies'
            ccount = str(uses) + ' ' + uname #e.g. 3 pennies
            ulist.append(ccount) #used coins + how many uses of said coin
    for i in range(len(ulist)):
        counted += ulist[i] #counted is final count
        if i == len(ulist) - 2:
            counted += ' and ' #adds "and" if it's last
        elif i < len(ulist) - 1:
            counted += ', ' #adds "," if it isn't last
    if counted == '':
        counted = 'nothing' #returns "nothing" rather then blank space if there's nothing
    return counted

penny = coin('penny',19.05,'copper plated steel', 1)
nickel = coin('nickel',21.2,'nickel plated steel',5)
dime = coin('dime',18.03,'nickel plated steel',10)
quarter = coin('quarter',23.88,'nickel plated steel',25)
loonie = coin('loonie',26.5,'brass plated steel',100)
toonie = coin('toonie',28,'aluminum-bronze center and a nickel plated steel ring',200)

cointypes = [toonie,loonie,quarter,dime,nickel,penny] #up to down
coinnames = [x.name for x in cointypes] #names of coins
coins = []
balance = 0
play = True
u = 'help'

while play:
    if u == 'help':
        print('commands are "total" to view total balance, "help" to see commands and "quit" to quit')
        print('coins are penny, nickel, dime, quarter, loonie and toonie')
    print('')
    u = input('enter a command or a coin (enter "help" to see avaiable commands): ')
    print('')
    valid = False #command is invalid
    if u == 'total':
        print('You currently have ' + countcoins([i.name for i in coins],cointypes) + ', totalling ' + str(balance) + ' cents.')
        valid = True
    elif u == 'quit':
        play = False
        valid = True
    elif u != 'help':
        for x in cointypes: 
            if u == x.name: #if command is a coin
                valid = True #it is valid
                print(x) #print str of coin
                coins.append(x) #add coins to list
                balance += x.value #add value to balance
        if not valid: #invalid command
            print('that command is not valid.')
            print('valid commands are "total" and "quit"')
            print('coins are penny, nickel, dime, quarter, loonie and toonie.')

play = True
while play:
    target = input('enter an amount to know how many coins are required to make said amount: ')
    if target == 'quit':
        play = False
    try:
        target = int(target)
        reqd = reqdcoins(target,cointypes) #required coins to make amount
        counted = countcoins(reqd,cointypes) #organizing coins into string
        print(str(target) + ' cents can be made of ' + counted + '.')
    except:
        if target != 'quit':
            print('input is not valid')
    