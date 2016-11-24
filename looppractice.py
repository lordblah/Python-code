def loop(x,y):
    number = [] #this is where i store the values
    x = 0 #made the variable x a local variable
    while x < y: #Exectures number of times , adding vaule to x till while is false
        print "At the top x is %d" %x
        number.append(x)

        x += 1
        print "Numbers now: ", number
        print "At the bottom i is %d" %x

loop(0,5)
