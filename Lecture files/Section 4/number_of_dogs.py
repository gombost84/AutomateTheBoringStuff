def numberofDogs():
    print('How many dogs do you have?')
    numDogs = input()
    try:
        if int(numDogs) < 0:
            print('That is a negative number. Try again.')
            numberofDogs()
        elif int(numDogs) == 0:
            print('You should get one.')
        elif int(numDogs) >= 4:
            print('That is a lot of dogs.')
        else:
            print('That is not that many dogs.')

    except ValueError:
        print('You did not enter a number. Try again!')
        numberofDogs()

numberofDogs()
