import re


def logs():
    with open("assets/logdata.txt", "r") as file:
        pattern = '''
        (?P<host>(\d*\.){3}\d*)
        (\ -\ )
        (?P<user_name>[-\w]*)
        (\ \[)
        (?P<time>\d*.*)
        (\]\ \")
        (?P<request>\w*.*)
        (\".*)'''
        dictionary = []
        for item in re.finditer(pattern, logdata, re.VERBOSE):
            dictionary.append(item.groupdict())

        return dictionary

print(len(logs()))

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
print(one_item in logs(), "Sorry, this item should be in the log results, check your formating")