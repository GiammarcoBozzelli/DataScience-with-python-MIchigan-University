import re
def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()
        pattern ='''(?P<name>\w*\s\w*)(\:\sB)'''
        l=[]
        for item in re.finditer(pattern, grades, re.VERBOSE):
            l.append(item.group(1))
        return l

print (len(grades()))
