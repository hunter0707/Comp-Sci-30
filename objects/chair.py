class chair:
    def __init__(self, color, material, legs, price):
        self.color = color
        self.material = material
        self.legs = legs
        self.price = price
    def printChair(self):
        print("A " + self.color + ' ' + self.material + ' chair that has ' + self.legs + ' legs and costs $' + self.price)

makeChair = True

while makeChair:
    color = input('What color should the chair be?: ')
    material = input('What should the chair be made of?: ')
    legs = input('how many legs does the chair have?: ')
    price = input('how much should the chair cost?: ')
    chairs = []
    
    if color == '':
        color = 'brown'
    if material == '':
        material = 'wood'
    if price == '':
        price = '0'
    if legs == '':
        legs = '4'

    chairs.append(chair(color,material,legs,price))
    for i in chairs:
        i.printChair()
    p = input('play again?: ')
    if p == 'no':
        makeChair = False