spam = 'hello world!'
print(spam.upper())
print(spam)

print(spam.upper().islower())
print(spam.isupper())

print(spam.isalpha())
print(spam.isalnum())
print('12345'.isdecimal())
print(' '.isspace())

print(spam.title())

spam = ['cats', 'bats', 'rats']

print(', '.join(spam))

spam = 'Hello'

print(spam.rjust(10))
print(spam.ljust(10))

print(spam.rjust(10, '*'))
print(spam.ljust(10, '-'))
print(spam.center(10, ':'))

print(spam.rjust(10).strip())

print('    x     '.rstrip())

spam = 'hello world!'
print(spam.replace('l', ':-:'))
