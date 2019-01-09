formatter = "%r %r %r %r" #defines the formatter as a string of %r four times.

print formatter % (1, 2, 3, 4) #prints the formatter using 4 MATH numbers
print formatter % ("one", "two", "three", "four") #using the formatter prints 4 strings
print formatter % (True, False, False, True) #using the formatter prints True/False 4 times.
print formatter % (formatter, formatter, formatter, formatter) #prints the formatter, defined as the string "%r %r %r %r", 4 times.
print formatter % (#using the formatter prints 4 strings
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "So I said goodnight."
)
