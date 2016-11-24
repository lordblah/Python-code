__author__ = 'Chaarles'
print "Let's practice everything."
print 'you\'d need to know \' bout escaped with \\ that do \n newlines and \t tabs.'

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \nthe need of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none
"""
print "----------------"
print poem
print "----------------"
#calculates and stores value into variable
five = 10 -2 +3 -6
print "This should be five: %s" % five

def secret_formula(started): # calculates how jars & crates can be used from the amount of beans
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    creates = jars / 100
    return jelly_beans, jars, creates

start_point = 10000 # initial starting amount
beans, jars, crates = secret_formula(start_point) # stores the return values jelly_beans, jars, crate
#one way to print out return variables from a function
print "With a starting point of: %d" % start_point
print "we'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
#another way to return and print vaibles from a functions
start_point = start_point / 10
print "we can also do thar this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)