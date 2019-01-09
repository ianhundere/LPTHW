# defines the function, cheese_and_crackers,
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints the string with the included formatter %d for an upcoming number.
    print "You have %d cheeses!" % cheese_count
    # " ^ "
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # prints a string.
    print "Man that's enough for a party!"
    # prints string and then jumps to new line.
    print "Get a blanket.\n"

# prints a string.
print "We can just give the function numbers directly:"
# call function assigning numbers to each
cheese_and_crackers(20, 30)
# print string
print "OR, we can use variables from our script:"
# define variables to be called for in the function.
amount_of_cheese = 10
amount_of_crackers = 50
# call function while including the variables defines earlier
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print string
print "We can even do math inside too:"
# call function and assign numbers through math
cheese_and_crackers(10 + 20, 5 + 6)

# print string
print "And we can combine the two, variables and math:"
# call function and assign numbers through both variables / math
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
