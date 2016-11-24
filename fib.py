__author__ = 'Chaarles'
from sys import argv

scrip, to_file = argv

def fib(n): #write fibonacci series up to n
    "print a fibonacci series uo to n"
    a, b = 0,1
    while a < n :
        print a,
        a, b = b, b +a

out_file = open(to_file, 'w')
out_file.write(str(fib(2000)))

out_file.close()


