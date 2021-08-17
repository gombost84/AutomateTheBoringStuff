import re

def regex_strip(str, strip = None):
    if strip == None:
        print(re.sub(r' (\w) ', r'\1', str))


regex_strip(' exactly ')