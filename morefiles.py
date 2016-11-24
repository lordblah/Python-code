__author__ = 'Tapatiolookalike'
from sys import argv
from os.path import exists
# Exists, returns True if a file exist, based on its name in a string as an argument.
#it returns False if not.
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we coukd do these two on one too, how
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)


#open, with "w" enables the file to be written in.
out_file = open(to_file, 'w')
# .write method, writes whatever string is in the parameter, wheth hardcoded or string from anthoer file
out_file.write(indata)

print "Alright, all done."

#.close fress up any system resources taken up by the open file. after calling the method .close\
#any attempts to use the file object will automaticaaly fail
out_file.close()
in_file.close()
