# assign the integer of 100 to the cars variable
cars = 100
# assign the float of 4.0 to the space_in_a_car variable
space_in_a_car = 4
# assign the integer of 30 to the drivers variable
drivers = 30
# assign the integer 90 to the passengers variable
passengers = 90
# assign the subtraction of drivers from cars to the cars_not_driven variable
cars_not_driven = cars - drivers
# assign cars_driven to drivers because the drivers can only drive one car each
cars_driven = drivers
# the carpool_capacity variable contains the amount of cars driven by the amount of seats in a car held int he space_in_a_car variable
carpool_capacity = cars_driven * space_in_a_car
# therefore, the average_passengers_per_car is the passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven

# print all relevant information
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
