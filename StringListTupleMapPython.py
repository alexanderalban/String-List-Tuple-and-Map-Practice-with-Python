# Regular string using ""
gorilla = "Why do gorillas have big nostrils? Big fingers!"
print(gorilla)

# Regular string using ''
pink = 'What is pink and fluffy? Pink fluff!'
print(pink)

# Multiline string using '''
bills = '''How do dinosaurs pay their bills?
With Tyrannosaurus checks!'''
print(bills)

# Preventing errors using '''
silly_string = '''He said, "Aren't can't shouldn't wouldn't."'''
print(silly_string)


# Escaping strings using \ (Not best practice for all strings, but still.)
single_quote_string = 'He said, "Aren\'t, can\'t, shouldn\'t, wouldn\'t."'
double_quote_string = "He said, \"Aren't, can't, shouldn't, wouldn't.\""

print(single_quote_string)
print(double_quote_string)

# Embedding values using %s
my_score = 1000
message = 'I scored %s points'
print(message % my_score)

# Replacing embedded value example
joke_text = '%s: a device for finding furniture in the dark'
bodypart1 = 'Knee'
bodypart2 = 'Shin'
print(joke_text % bodypart1)
print(joke_text % bodypart2)

# Using more than one placeholder in a string
nums = 'What did the number %s say to the number %s? Nice belt!'
print(nums % (0, 8))

# Multiplying strings
spaces = ' ' * 25
print('%s 12 Burts Wynd' % spaces)
print('%s Twinkebottom Heath' % spaces)
print('%s West Snoring' % spaces)
print()
print()
print('To Whom It May Concern')
print()
print('Hello.')
print()
print('XOXO')
print("Anonymous")

print(1000 * 'boop')

# Lists!

wizard_list = ['spider legs', 'toe of frog', 'eye of newt',
               'bat wing', 'slug butter', 'snake dandruff']
print(wizard_list)

# Single out list item
print(wizard_list[2])

# Change item in list
wizard_list[2] = "snail tongue"
print(wizard_list)

# Subset of items
print(wizard_list[2:5])

# List within a list
numbers = [1, 2, 3, 4]
strings = ['I', 'kicked', 'my', 'toe', 'and', 'it', 'is', 'sore']
myList = [numbers, strings]
print(myList)

# Add items to a list
wizard_list.append('bear burp')
print(wizard_list)

wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
print(wizard_list)

# Remove items from a list
del wizard_list[5]
print(wizard_list)

del wizard_list[8]
del wizard_list[7]
del wizard_list[6]
print(wizard_list)

# Joining Lists
list1 = [1, 2, 3, 4]
list2 = ['I', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
print(list1 + list2)

list3 = list1 + list2
print(list3)

list4 = [1, 2]
print(list4 * 5)
