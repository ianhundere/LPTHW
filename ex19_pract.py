def worry_not (kaboodles, noodles):
    print "All is well when %s are there to save the day." % kaboodles
    print "%s are mighty delicious too if you eat them in the morning." % noodles
    print "That sure was interesting!"
    print "Night, night.\n"

print "Now look closely:"
worry_not(20, 30)

print "OR, we can use variables from our script:"
amount_of_kaboodles = 10
amount_of_noodles = 50
worry_not(amount_of_kaboodles, amount_of_noodles)

print "Let's try mixing it up with both variables and numbers:"
worry_not(amount_of_kaboodles+1, amount_of_noodles+2)

print "So, you want it different now, do ya? I'll give you different."
worry_not(5, 2)
worry_not(5+2, 8+9)
kaboodles = "yum yum."
noodles = "eww, eww."
worry_not("%s" % kaboodles, "%s" % noodles)
worry_not(12-5, 6-8)
ka = "BAM!"
no = 9
worry_not("%s Are you okay?" % ka, "%d is a sham." % no)

day = raw_input("On a scale from 1-10, what kind of day is it outside?")
tall = raw_input("How many feet tall are you?")
worry_not(day, tall)

apples =  "apples"
oranges = "Oranges"
worry_not("%s" % apples, "%s" % oranges)
