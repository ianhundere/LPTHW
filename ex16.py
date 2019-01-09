#says to use arguments found in the sys module.
from sys import argv
#script always represents the name of the py program / filename is found as arg
script, filename = argv
#prints 3 strings, 1st string includes a string formatting operation, see all.
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#before opening the file, it asks for input.
raw_input("?")
#opens the file in write mode.
print "Opening the file..."
target = open(filename, 'w')
#truncates the file but not necessary since the file is truncated in write mode.
print "Truncating the file. Goodbye!"
target. truncate()
#prints the below string
print "Now I'm going to ask you for three lines."
#asks for data from the user.
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
#prints the string below
print "I'm going to write these to the file."
#instead of writing target.write 3 times, use %s to format string with 3 inputs.
target.write("%s\n%s\n%s\n" % (line1, line2, line3))
#prints the below string.
print "And finally, we close it."
#closes the file
target.close()
