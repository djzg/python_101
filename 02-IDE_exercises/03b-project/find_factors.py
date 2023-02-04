'''
Write a Python program that prompts the user to enter a positive integer, then output all the positive integers that
divisible by that number, including itself and 1, in ascending order. The program should match the following format when
it is executed.
'''

pos_int = int(input('Please enter a positive integer: '))

print('The factors of 12 are: ')
for i in range(1, pos_int + 1, 1):
    if pos_int % i == 0:
        print(i)

