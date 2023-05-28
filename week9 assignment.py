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