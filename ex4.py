#explains that the variable car means 100
cars = 100
#defines the amount of space in the car, 4.0.
space_in_a_car = 4.0
#defines the variable of drivers, 30.
drivers = 30
#defines the variable of passengers, 90.
passengers = 90
#defines the variable of cars_not_driven, that is, cars - drivers(100-30).
cars_not_driven = cars - drivers
#defines the variable of cars_not_driven as 100 - 30 (or cars - drivers)
cars_driven = drivers
#defines the variable of carpool_capacity as cars_driven/drivers * space_in_a_car/40.
carpool_capacity = cars_driven * space_in_a_car
#defines the variable average_passengers_per_car as passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
