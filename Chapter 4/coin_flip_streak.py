##For this exercise, we’ll try doing an experiment.
##If you flip a coin 100 times and write down an “H”
##for each heads and “T” for each tails, you’ll create
##a list that looks like “T T T T H H H H T T.”
##If you ask a human to make up 100 random coin flips,
##you’ll probably end up with alternating head-tail results
##like “H T H T H H T H T T,” which looks random (to humans),
##but isn’t mathematically random. A human will almost never
##write down a streak of six heads or six tails in a row,
##even though it is highly likely to happen in truly random
##coin flips. Humans are predictably bad at being random.
##
##Write a program to find out how often a streak of six heads
##or a streak of six tails comes up in a randomly generated
##list of heads and tails. Your program breaks up the experiment
##into two parts: the first part generates a list of randomly
##selected 'heads' and 'tails' values, and the second part checks
##if there is a streak in it. Put all of this code in a loop that
##repeats the experiment 10,000 times so we can find out what
##percentage of the coin flips contains a streak of six heads or
##tails in a row.

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flipList = []
    flipCounter = 0
    while flipCounter < 100:
        currentFlip = random.randint(0,1)
        if currentFlip == 0:
            flipList.append('T')
        else:
            flipList.append('H')
        flipCounter += 1

    # Code that checks if there is a streak of 6 heads or tails in a row.
    streakCounter = 0
    while streakCounter < len(flipList) - 5:
        if (flipList[streakCounter] == flipList[streakCounter + 1]
        == flipList[streakCounter + 2] == flipList[streakCounter + 3]
        == flipList[streakCounter + 4] == flipList[streakCounter + 5]):
            numberOfStreaks += 1
            streakCounter += 1
        else:
            streakCounter += 1
            
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
