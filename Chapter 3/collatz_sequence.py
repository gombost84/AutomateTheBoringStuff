#Write a function named collatz() that has one parameter named number.
#If number is even, then collatz() should print number // 2 and return this value.
#If number is odd, then collatz() should print and return 3 * number + 1.
#Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1.
#Add try and except statements to the previous project to detect whether the user types in a noninteger string.
#normally, the int() function will raise a valueerror error if it is passed a noninteger string, as in int('puppy').
#in the except clause, print a message to the user saying they must enter an integer.

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
