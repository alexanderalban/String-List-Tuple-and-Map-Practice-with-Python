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

# Lists! Lists of strings and numbers

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

# Tuples! Like lists, but with () and cannot be edited
fibs = (0, 1, 1, 2, 3)
print(fibs[3])

# Maps! Lists that have keys and values (think dictionary - every word has a definition -- key, value)

favorite_sports = {'Ralph Williams': 'Football',
                   'Michael Tippett': 'Basketball',
                   'Edward Elgar': 'Baseball',
                   'Rebecca Clarke': 'Netball',
                   'Ethel Smyth': 'Badminton',
                   'Frank Bridge': 'Rugby'}

print(favorite_sports['Rebecca Clarke'])

# Deleting map items
del favorite_sports['Ethel Smyth']
print(favorite_sports)

# Repace value in map
favorite_sports['Ralph Williams'] = 'Ice Hockey'
print(favorite_sports)


# Random Practice!

# combine lists
hobbies = ['hockey', 'games', 'driving', 'music', 'puzzles']
foods = ['peanuts', 'peppers', 'bananas', 'sprouts']
combined = hobbies + foods
print(combined)

# counting combatants
# If there are 3 buildings with 25 ninjas hiding on each roof and 2 tunnels with 40 samurai hiding in each tunnel,
# how many ninjas and samurai are about to do battle?

fighters = 3 * 25 + 2 * 40
print(fighters)

# Using Variables

adjective = 'Power'
noun = 'Rangers'
catchphrase = 'Go, Go, %s %s!'
print(catchphrase % (adjective, noun))




# ##### More Practice with Python Crash Course

# modifying objects in a list

motorcycles = ['honda', 'mitsubishi', 'yamaha']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# append to add an item to the end of a list
motorcycles.append('honda')
print(motorcycles)

# building lists from scratch using append
xmen = []
xmen.append('cyclops')
xmen.append('rogue')
xmen.append('beast')
xmen.append('jean grey')
print(xmen)

# insert elements into a list using the insert() method
xmen.insert(2, 'wolverine')
print(xmen)

# removing items from a list using the del method. this completely removes the variable, making it unusable
del xmen[2]
print(xmen)

# removing items with pop() allows us to still use the variable when we need to. by default, pop removes from the end of a list. we can also specify the index to remove
# a specific item

xmen = ['cyclops', 'jean grey', 'beast', 'rogue', 'storm', 'wolverine']
inactive_xmen = []

xmen.pop()
xmen.pop(3)

print(xmen)

# remove allows us to remove a specific value from a list
xmen.remove('jean grey')
print(xmen)

# sorting a list. using sort() will let us alphabetize a list

avengers = ['iron man', 'thor', 'captain america', 'hulk', 'black widow', 'hawkeye']
avengers.sort()
print(avengers)

# we can also go in reverse order, by specifying reverse = True

avengers.sort(reverse=True)
print(avengers)

# we can temprarily sort a list using sorted()

print(sorted(avengers))
print(avengers)

# we can reverse the order of a list using reverse()
avengers.reverse()
print(avengers)

print(len(avengers))