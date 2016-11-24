def isPhoneNumber(text):
    if len(text) != 12: #checks length of characters,
        return False
    for i in range(0,3):#checks first three chartecters if their decsimals
        if not text[i].isdecimal():
            return False
    if text[3] != '-': #checks for hyphen
        return False
    for i in range(4, 7): #checks next three digits for decimals
        if not text[i].isdecimal():
            return False
    if text[7] != '-':# checks for hyphen in the seventh slot
        return False
    for i in range(8,12): #checks last digits for decimal
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print (isPhoneNumber(u'415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber(u'moshi moshi'))

message = 'Call me at' + u'415-555-1011 tomorrow.' + u'415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i +12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
    print('Done')