x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# two strings are nested inside a parent string here
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# a string is nested inside a parent string here
print "I said: %r." % x
# a string is nested inside a parent string here
print "I also said: '%s'." % y

hilarious = False
# although this isn't a nested string, it could be considered one almost because False isn't an integer
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
