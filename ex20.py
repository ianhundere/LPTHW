# imports argv to use from sys
from sys import argv
# unpacks arguments for script/input_file variables
script, input_file = argv
# defines print_all function. takes 1 argument, (f)
def print_all(f):
# prints what's in f
    print f.read()
# define function to rewind. the file's current position (default to 0)
def rewind(f):
    f.seek(0)
# defines a function that uses two argument (line_count, f)
def print_a_line(line_count, f):
    # print line_count and then a line from the f file
    print line_count, f.readline()
# set current_file variable to a file pointer to input_file
current_file = open(input_file)
# prints string
print "First let's print the whole file:\n"
# call print_all function with current_file as an argument
print_all(current_file)
# prints string
print "Now let's rewind, kind of like a tape."
# calls rewind function with current_file as argument
rewind(current_file)
# print string
print "Let's print three lines:"
# set current_line to 1
current_line = 1
# call a print_a_line function with current_line and current_file as arguments
print_a_line(current_line, current_file)

# set current_line to itself + 1
current_line = current_line + 1
# call print_a_line function with current_line and current_file as arguments
print_a_line(current_line, current_file)

# set current line to itself + 1
current_line = current_line + 1
# call print_a_line with current_line and current_file as arguments
print_a_line(current_line, current_file)
