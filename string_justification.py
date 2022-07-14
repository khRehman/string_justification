'''#python strings support justification. What that means is that you can center
 a string or right or left justify a string, you only need to tell python how long the string needs to be'''

s = "welcom to python Strings"


# center justification
print(s.center(30))


# right justification
print(s.rjust(30))

# left justification
print(s.ljust(30))