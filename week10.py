print('Welcome to Luc\'s Online Store')
print()

names = []
prices = []

option = 0
while option != 5:
    print()
    print('Shopping cart menu: ')
    print('1. Add a new item')
    print('2. View cart')
    print('3. Remove an item')
    print('4. Compute total')
    print('5. Quit')
    print()

    option = int(input('Enter your choice: '))

    if option == 1:
        new_item = input('What item would you like to add? ')
        price = float(input(f'What is the price of \'{new_item}\'? '))
        names.append(new_item)
        prices.append(price)
        print(f'\'{new_item}\' has been added to the cart.')

    if option == 2:
        print()
        print('The contents of the shopping cart are: ')
        item_number = 1
        for name, price in zip(names, prices):
            print(f'{item_number}. {name} - ${price:.2f}')
            item_number += 1

    if option == 3:
        print()
        item_number = int(input('What item would you like to remove? '))
        if item_number <= len(names):
            del names[item_number - 1]
            del prices[item_number - 1]
            print('Item removed.')
        else:
            print('Sorry, that is not a valid item number.')
        print()

    if option == 4:
        print()
        total_price = 0
        for price in prices:
            total_price += price
        print(f'The total price of the items in the shopping cart is ${total_price:.2f}')
        print()

print('Thank you. Goodbye.')