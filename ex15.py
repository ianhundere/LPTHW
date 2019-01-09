from sys import argv#uses a module to collect info from the user via the commandline.
#determines argv's arguments...script is typically first.
script, filename = argv
#the open function takes a parameter and returns a value; filename.
txt = open(filename)
#prints our filename
print "Here's your file %r:" % filename
print txt.read() #prints a function txt, without parameters, just read.
txt.close()
#prints the filename we inputted earlier on the commandline
print "Type the filename again:"
file_again = raw_input("> ")#prompts user to input file again.

txt_again = open(file_again)#based on user's input, the open function/methods
#opens file
print txt_again.read()#as before, file is printed using the txt function with
#parameters, just read.
txt_again.close()
