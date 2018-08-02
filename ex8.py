formatter = '{} {} {} {}'

print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
# I add space (on this line) bc the formatter does this
# between curly brackets. Changing the end parameter in the print function doesn't
# do anything because the formatted string is a single function.
  ' I live to fight\n',
  'Give me a tool like a blade\n',
  'I\'ll work with it\n',
  'Until my fortunes are made\n'
))
