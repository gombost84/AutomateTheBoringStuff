#Write a function named printTable() that takes a list of lists of strings
#and displays it in a well-organized table with each column right-justified.
#Assume that all the inner lists will contain the same number of strings.
#For example, the value could look like this:

#tableData = [['apples', 'oranges', 'cherries', 'banana'],
#             ['Alice', 'Bob', 'Carol', 'David'],
#             ['dogs', 'cats', 'moose', 'goose']]

#Your printTable() function would print the following:

#   apples Alice  dogs
#  oranges   Bob  cats
# cherries Carol moose
#   banana David goose

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):

    colWidth = [0] * len(tableData)

    n = 0

    while n < len(table):
        for length in table[n]:
            if len(length) > colWidth[n]:
                colWidth[n] = len(length)
        n += 1

    for word in range(len(table[0])):
        for item in range(len(table)):
            print(table[item][word].rjust(colWidth[item]), end=' ')
        print()

print_table(tableData)