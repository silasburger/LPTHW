# declaring cars variable
cars = 100
# declaring space in cars variable. It is a floating point number
space_in_cars = 4
# declaring drivers variable
drivers = 30
# ditto passengers ditto
passengers = 90
# subratract drivers from cars to equal new variable cars_driven
cars_not_driven = cars - drivers
# declare cars_driven to equal drivers
cars_driven = drivers
# declare carpool_capacity to equal product of cars driven and space_in_cars
carpool_capacity = space_in_cars * cars_driven
# declare average passengers per car to equal passengers / carpool_capacity
average_space_per_car = passengers / cars_driven

print("There are", cars, "cars availible.")
print("There are only", drivers, "drivers availible.")
print("There will be", cars_not_driven, "empry cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_space_per_car, "in each car.")
