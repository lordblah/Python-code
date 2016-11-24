ten_things = "Apples Oranges Crows Telephone Light Surgar"
print "Wait there's not 10 things in that list, let's fix that."

#split returns a list of the string sentence
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Fresbee", "Corn", "Banana", "Girl", "Boy"]

#len is measure length or qunatiy of the variable
while len(stuff) != 10:
    next_one = more_stuff.pop() #pop, remvoes the list item in the list and returns it
    print "Adding: ", next_one
    stuff.append(next_one) #adds new word from next_one to stuff variable
    print "there's %d items now." %len(stuff)

print "there we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print stuff
print ' '.join(stuff) #adds a space between the list
print '#'.join(stuff[3:5]) #adds # between strings 3 and 5


