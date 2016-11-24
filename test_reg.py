import re

britishPhoneNumber = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
mo = britishPhoneNumber.search('Here\\s a phone number from london 020-4643-9587')
print('Phone number found: ' + mo.group())