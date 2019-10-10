input('object')

#object
class menu:
    def __init__(self, name, desc, gluten, price):
        self.name = name
        self.desc = desc
        self.gluten = gluten
        self.price = price
    def printMenu(self):
        print('Item: ' + self.name)
        print('Description: ' + self.desc)
        print('Gluten Free: ' + str(self.gluten))
        print('Price: $' + str(self.price))
        print('')

menuItems = [] #menu items
menuItems.append(menu('Chicken Wings', 'Perfectly breaded chicken wings fried to a crispy golden brown', False, 22.99)) #item name, desc, gluten free, price
menuItems.append(menu('Hot Water', 'Perfectly boiled water served in a mug', True, 5.5))
menuItems.append(menu('Warm Water', 'Water poured into a cup and microwaved to luke warm mediocrity', True, 5.25))
menuItems.append(menu('Cold Water', 'Crisp cold water with a generous serving of ice', True, 5.75))
menuItems.append(menu('Grilled Cheese Sandwich', 'A slice of cheddar cheese between two slices of artisan toast', False, 12.99))
menuItems.append(menu('Spaghetti', 'spaghetti cooked al dente with freshly made pasta sauce', False, 24.99))
menuItems.append(menu('Ravioli', 'Square ravioli served in pasta sauce', False, 24.5))
menuItems.append(menu('Fries', 'Freshly sliced potatoes, fried in canola oil to a crisp golden brown', False, 15.99))
menuItems.append(menu('Caesar Salad', 'A salad of romaine lettuce and croutons, in a light caesar dressing', False, 13.99))
menuItems.append(menu('Fish and Chips', 'Freshly battered cod and freshly sliced potatoes fried served with coleslaw', False, 22.5))

for i in menuItems:
    i.printMenu()

input('procedural')

#procedural
menuItems = ['Chicken Wings', 'Hot Water', 'Warm Water', 'Cold Water', 'Grilled Cheese Sandwich', 'Spaghetti', 'Ravioli', 'Fries', 'Caesar Salad', 'Fish and Chips']
menuDescriptions = ['Perfectly breaded chicken wings fried to a crispy golden brown', 'Perfectly boiled water served in a mug', 'Water poured into a cup and microwaved to luke warm mediocrity', 'Crisp cold water with a generous serving of ice', 'A slice of cheddar cheese between two slices of artisan toast', 'spaghetti cooked al dente with freshly made pasta sauce', 'Square ravioli served in pasta sauce', 'Freshly sliced potatoes, fried in canola oil to a crisp golden brown', 'A salad of romaine lettuce and croutons, in a light caesar dressing', 'Freshly battered cod and freshly sliced potatoes fried served with coleslaw']
glutenFree = [False, True, True, True, False, False, False, False, False, False]
menuPrices = [22.99, 5.50, 5.25, 5.75, 12.99, 24.99, 24.50, 15.99, 13.99, 22.50]

for i in range(10):
    print('Item: ' + menuItems[i])
    print('Description: ' + menuDescriptions[i])
    print('Gluten Free: ' + str(glutenFree[i]))
    print('Price: $' + str(menuPrices[i]))
    print('')