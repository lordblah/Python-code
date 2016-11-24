from sys import argv

script, input_file = argv


def print_all(f):
    print f.read()

# .seek method chooses where you would like to start from 0 being the first byte character
def rewind(f):
    f.seek(0)
# .readline() reads a single line from the file; a newline character (\n) is left at the end of the string,

def print_a_line(line_count, f):
    print line_count, f.readline()
#assigns file to varialbe
current_file = open(input_file)

print "First lets print the whole file: \n"
#prints the strings in input file
print_all(current_file)

print "Now let's rewind, kind of like a tape"
#used .seek to start at the beigging string of the file
rewind(current_file)

print "Lets print three lines:"

current_line = 1
print_a_line(current_line, current_file) # print line info of what line, prints string line

current_line = current_line +1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)