
count_of_numbers = int(input('How many numbers would you like to enter?'))

print(f'Please enter {count_of_numbers} numbers:')

min = None
max = None

for i in range(1, count_of_numbers + 1):
    number = int(input(f'Please enter {str(i)} number(s): '))

    if min is None or number < min:
        min = number
    if max is None or number > max:
        max = number

print(f'min: {min}')
print(f'max: {max}')