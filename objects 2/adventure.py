import random

class hero:
    def __init__(self,name,health,energy,dexterity,power):
        self.name = name 
        self.health = health 
        self.energy = energy 
        self.dexterity = dexterity
        self.power = power
        self.equipped = [] #list of equipped items
        self.bag = backpack(self.name)
    def pickup(self,item):
        self.bag.place(item)
    def equip(self,item):
        def Equip(item):
            self.bag.items.remove(item) #removes from bag
            self.bag.capacity += item.weight #adds capacity back to bag
            self.bag.capacity = round(self.bag.capacity,2) #rounds to 2 decimal places
            self.equipped.append(item) #added to equipped
            print('You equip ' + item.name + ' successfully!')
        if item in self.bag.items: #item in bag
            if len(self.equipped) == 0: #no items equipped
                Equip(item)
            elif self.equipped[0].twohanded and len(self.equipped) == 1: #less then 2 items but first item is 2 handed
                print(self.equipped[0].name + ' is two handed and you cannot equip ' + item.name + '!') 
            elif len(self.equipped) == 2: #2 items equipped
                print('You already have {} and {} equipped and cannot equip any more items'.format(self.equipped[0].name,self.equipped[1].name))
            else:
                Equip(item)
        else:
            print(item.name + ' is not in your bag!')
    def attack(self,weapon):
        rdmg = random.randint(1,10)
        try:
            dmg = weapon.power + rdmg
        except:
            dmg = self.power + rdmg
        if rdmg > self.dexterity: #damage greater then dexterity means a miss
            dmg = 0
            print('Your attack fails, doing no damage.')
        else:
            print('You attack, doing ' + str(dmg) + ' damage.')
    def __str__(self):
        string =  '{}: \nhealth: {} \nenergy: {} \ndexterity: {} \npower: {} \n'.format(self.name,self.health,self.energy,self.dexterity,self.power)
        if len(self.equipped) == 1:
            string += self.equipped[0].name + ' is equipped.'
        elif len(self.equipped) == 2:
            string += '{} and {} are equipped.'.format(self.equipped[0].name, self.equipped[1].name)
        else:
            string += 'No items are equipped.'
        return(string)
        
class backpack:
    def __init__(self,owner):
        self.owner = owner
        self.capacity = round(random.uniform(25,35),2) #25-35, rounded to 2 decimals
        self.weight = round(random.uniform(1.5,3),2) #1.5-3, rounded to 2 decimals
        self.material = random.choice(['canvas','fabric','cloth','cotton']) #1 of 4 materials
        self.items = []
    def place(self,item):
        if self.capacity - item.weight >= 0: 
            self.items.append(item)
            self.capacity -= item.weight
            self.capacity = round(self.capacity,2)
            print('You place {} in your bag, using {} capacity, {} capacity remains.'.format(item.name,item.weight,self.capacity))
        else:
            print('The item does not fit in your bag! {} takes {} space but you only have {}.'.format(item.name,item.weight,self.capacity))
    def __str__(self):
        string = "{}'s bag has a capacity of {} \n".format(self.owner,self.capacity)
        string += 'It has a weight of {} and it is made of {}. \n'.format(self.weight,self.material)
        if len(self.items) >= 1:
            string += 'It contains {} items, {} capacity remains, the items are the following: '.format(len(self.items),self.capacity)
            for i in self.items:
                if i == self.items[len(self.items)-1]:
                    string += i + '.'
                else:
                    string += i + ', '
        else:
            string += 'No items are in the bag.'
        return(string)

class weapon:
    def __init__(self,name,variety,power,equipped,weight):
        self.name = name
        self.variety = variety 
        self.power = power 
        self.equipped = equipped
        self.weight = weight

class sword(weapon):
    def __init__(self,name,variety,power,equipped,weight,twohanded):
        weapon.__init__(self,name,variety,power,equipped,weight)
        self.twohanded = twohanded

class shield(weapon):
    def __init__(self,name,variety,power,equipped,weight,defense):
        weapon.__init__(self,name,variety,power,equipped,weight)
        self.defense = defense

BroadswordOfWidth = sword('the Broadsword of Width','broadsword',8,False,6.78,True)
LongswordOfLength = sword('the Longsword of Length','longsword',9,False,7.12,True)
RapierOfPointiness = sword('the Rapier of Pointiness','rapier',7,False,4.56,False)
WoodenShield = shield('the Shield of Splinters','shield',4,False,5.67,5)
IronShield = shield('the Shield of Irony','shield',8,False,10.24,5)
RiotShield = shield('the Shield of Riots','shield',6,False,12.5,6)
Magnus = hero('Magnus',10,10,random.randint(4,10),random.randint(3,5))

print(Magnus)
print(Magnus.bag)
Magnus.pickup(RapierOfPointiness)
Magnus.pickup(IronShield)
Magnus.equip(RapierOfPointiness)
Magnus.equip(IronShield)
Magnus.equip(RiotShield)
print(Magnus)