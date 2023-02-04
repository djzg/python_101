amount = int(input('Please enter an amount between 0 and 99 cents: '))

quarter = 25
dime = 10
nickel = 5
penny = 1

quarters = amount // quarter
dimes = (amount % quarter) // dime
nickels = ((amount % quarter) % dime) // nickel
pennies = (((amount % quarter) % dime) % nickel)

print('Your change will be: ')
print(f'Q: {quarters}')
print(f'D: {dimes}')
print(f'N: {nickels}')
print(f'P: {pennies}')

