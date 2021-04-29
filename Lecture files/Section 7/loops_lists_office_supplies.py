for i in range(4):
    print(i)

for i in [0, 1, 2, 3]:
    print(i)

print(len(range(4)))

spam = list(range(4))
print(spam)

spam = list(range(0, 101, 2))
print(spam)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' +  str(i) + ' in supplies is: ' + supplies[i])
