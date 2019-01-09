tabby_cat = "\tI'm tabbed in." # escape single-quote inside string
persian_cat = "I'm split\non a line." # escape new line character
backslash_cat = "I'm \\ a \\ cat." # escape backslash

# anything after """ is treated as a string. then \t indents/tabs each line. \n creates a new line character.
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat #prints variable which represents string.
print persian_cat #prints variable which represents string.
print backslash_cat #prints variable which represents string.
print fat_cat #prints variable which represents string.
