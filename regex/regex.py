'''
>>> check_email_edu()
True
>>> check_email_regular()
True
>>> check_email_negative()
False
'''

import re

pattern = "^(([^-#*])+(\.?))+@(([a-zA-Z])(\.?))+$"

def check_email_edu():
    email = "иеузфрт.enrique.mueller@uni.edu.de"
    regexp = re.compile(pattern)
    return regexp.search(email) is not None

def check_email_regular():
    email = "student1234@gmail.com"
    regexp = re.compile(pattern)
    return regexp.search(email) is not None

def check_email_negative():
    email = "#-*&12@com"
    regexp = re.compile(pattern)
    return regexp.search(email) is not None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
