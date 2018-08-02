print('How old are you?')
age = input('ENTER AGE IN YEARS:') # Assigns a variable to an input that users type into command line.

print('How tall are you?')
height = input('ENTER HEIGHT IN FEET:')

print('How much do you weigh?')
weight = input('ENTER WEIGHT IN POUNDS:');

print(f'So, you\'re {age} old, {height} feet tall, and pounds {weight} heavy.')

emotion = input('Type how you are feeling in one word: ')
print(f'So, you are feeling {emotion}.')

favorite_num = int(input('What is your favorite number?'))
half_favorite_num = favorite_num / 2
print('So, your half favorite number is {}'.format(half_favorite_num))
