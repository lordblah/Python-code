import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # compile returns an regrex pattern object
mo = phoneNumRegex.search('My phone number is 415-555-4242 and 412-134-1234 .')
#search method searches the string it is passed for any matches to the regex pattern object
#search method will return NONE id the pattern is not found in the string
#if the pattern is found, the serach method returns a match object.
#match objects have a group method that will return the actual matched text from the searched string.
print('Phone number found: ' + mo.group())

