## spam = ['apples', 'bananas', 'tofu', 'cats']
## Write a function that takes a list value as
## an argument and returns a string with all the
## items separated by a comma and a space, with
## and inserted before the last item. For example,
## passing the previous spam list to the function
## would return 'apples, bananas, tofu, and cats'.


spam = ['apples', 'bananas', 'tofu', 'cats']

def joining_lists(list):
    counter = 0
    string_to_print = ''
    while counter < len(list) - 2:
        string_to_print += list[counter] + ', '
        counter += 1
    string_to_print += list[-2] + ' and '
    string_to_print += list[-1]
    return string_to_print

if len(spam) != 0:
    print(joining_lists(spam))
    
else:
    print('The list has no items in it.')
