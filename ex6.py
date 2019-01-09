#defines a variable using a string and a formatter
x = "There are %d types of people." % 10
#defines the variable of binary
binary = "binary"
#defines the variable of do_not
do_not = "don't"
#defines a variable using a string and a formatter
y = "Those who know %s and those who %s." % (binary, do_not)

#prints the variable x
print x
#prints the variable y
print y

#tells the program to print a string
print "I said: %r." % x
#tells the program to print a string
print "I also said: '%s'." % y

#defines a variable, hilarious
hilarious = False
#defines a variable, joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

#tells the program to print the variable, joke_evaluation and hilarious
print joke_evaluation % hilarious

#defines a variable using a string
w = "This is the left side of..."
#defines a variable using a string
e = "a string with a right side."

#
print w + e
