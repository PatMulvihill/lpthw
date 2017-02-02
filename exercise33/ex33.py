howManyTimes = 60
numbers = []
incrementer = 10

def looper(howMany, increment):
    i = 0
    for i in range(0, howMany):
        print "At the top i is %d" % i
        numbers.append(i)
    
        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        
looper(howManyTimes, incrementer)
    
    
print "The numbers: "

for num in numbers:
    print num