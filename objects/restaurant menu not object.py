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