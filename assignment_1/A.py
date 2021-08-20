
import re
def names(string=None):
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    if string == None :
        return re.findall('[A-Z][a-z]*', simple_string)
    else:
        return re.findall('[A-Z][a-z]*', string)
    # raise NotImplementedError()
    #raise NotImplementedError()

print(len(names("""Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids.""")))