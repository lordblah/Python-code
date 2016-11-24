from sys import argv
#script is the name of program in command line, filename is name of file you want opened,
#which is typed after the script
#python input.py sample.txt, this is entered into command line
script, filename = argv
# open returns a file you want opened
txt = open(filename)
# prints my file name
print "Here's your file %r:" %filename
# read method reads some quantity of  data and returns it as a string. when size is ommited the entire contents is read

print txt.read()

print "type the filename again:"
#prompting the user to enter a file, they want opened or reopened
file_again = raw_input("> ")
#opening or reopening a file
txt_again = open(file_again)
#reads the contents of the file and prints it out
print txt_again.read()