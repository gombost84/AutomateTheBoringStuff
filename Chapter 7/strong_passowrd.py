
import re

text = """There is one tuple for each match, and each tuple Contains1 strings for each group in the regular expression. Remember that group 0 matches the entire regular expression, so the group at index 0 of the tuple is the one you are interested in.
"""

def strong_pass_check(pwd):
    
    passAlphanum = re.compile(r'\w{8,}')

    passDigit = re.compile(r'[0-9]')

    passLower = re.compile(r'[a-z]')

    passUpper = re.compile(r'[A-Z]')
    
    for x in passAlphanum.findall(pwd):
    
        if passDigit.search(x) is None:
            return False
        
        elif passLower.search(x) is None:
            return False
        
        elif passUpper.search(x) is None:
            return False

        else:
            return True


if strong_pass_check(text) == True:
    print('A OK')

else:
    print('Nope')