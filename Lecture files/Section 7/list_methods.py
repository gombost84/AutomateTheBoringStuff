spam = ['hello', 'hi', 'howdy', 'heyas', 'Ziiing']
print(spam)
print(spam.index('hello'))

spam.append('yo bruv')
print(spam)

spam.insert(1, 'eeyoo')
print(spam)

spam.remove('eeyoo')
print(spam)

del spam[-1]
print(spam)

spam.sort()
print(spam)

spam.sort(key=str.lower)
print(spam)

spam = [2, 5, 1, 3.14, -7]
print(spam)
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)
