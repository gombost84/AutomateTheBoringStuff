def collatz(number):
    if number == 1:
        print('The sequence is complete!')
    elif number % 2 == 0:
        print(number / 2)
        collatz(number / 2)
    else:
        print(3 * number + 1)
        collatz(3 * number + 1)

number2 = int(input('Enter a number: '))

try:
    collatz(number2)

except ValueError:
    print('Error! The entered value is not a number.')
