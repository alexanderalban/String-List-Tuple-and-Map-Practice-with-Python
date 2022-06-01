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
