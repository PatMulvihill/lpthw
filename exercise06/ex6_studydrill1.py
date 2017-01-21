# x is a variable that holds a string formatted with an integer
x = "There are %d types of people." % 10
# binary is a string that contains the word binary
binary = "binary"
# do_not is a variable holding the string "don't"
do_not = "don't"
# y is a string variable that contains a string formatted with two integers
y = "Those who know %s and those who %s." % (binary, do_not)

# print the formatted contents of x
print x
# print the formatted contents of y
print y

# print a repition of what just happened with nested strings
print "I said: %r." % x
print "I also said: '%s'." % y

# hilarious is a boolean variable containing False
hilarious = False
# joke_evaluation is a string variable that contains a boolean formatter
joke_evaluation = "Isn't that joke so funny?! %r"

# print joke_evaluation with hilarious as it's formatter parameter
print joke_evaluation % hilarious

# declare two strings that we will concatenate named w and e
w = "This is the left side of..."
e = "a string with a right side."

# print w and e added together, which just concatenates e to the end of the w string
print w + e
