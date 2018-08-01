types_of_people = 10 # Declared a variable and assigned a 10 to it
x = f"There are {types_of_people} types of people." # Declared a formatted string

binary = "binary" # Assigned a string to a variable
do_not = "don't" # Assigned a string to a variable
y = f"Those who know {binary} and those who {do_not}." # Declared a formatted string

print(x) # Printed the formatted string
print(y) # Printed the formatted string

print(f"I said {x}") # Printed the formatted string with a formatted string embedded in it
print(f"I also said: '{y}'") # Printed the formatted string with a formatted string embedded in it

hilarious = False # Assigned a boolean to a variable

joke_evaluation = "Isn't that joke so funny?! {}" # Assigned a string to a varaible with empty curly braces

print(joke_evaluation.format(hilarious)) #Adds the hilarious variable to the joke evaluation formatted string (where the empty curly braces are)

w = "This is the left side of..." # Assigns a string to w
e = "A string with a right side." # Assigns a string to e

print(w + e) # Concatinates w and e
