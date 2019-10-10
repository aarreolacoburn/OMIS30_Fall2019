# Class5 Homework
# author: midavis
# last modified: 2019-10-08
# OMIS 30 - Fall 2019 - HW5
# Create a menu dictionary of dictionaries...

# Real code
menu = dict()

menu['Monday'] = dict()
menu['Tuesday'] = dict()
menu['Wednesday'] = dict()
menu['Thursday'] = dict()
menu['Friday'] = dict()

menu['Monday']['breakfast'] = {'drink':'water', 'appetizer':'calimari', 'main':'steak', 'dessert':'ice cream'}
menu['Tuesday']['lunch'] = dict()
menu['Tuesday']['lunch']['drink'] = 'iced tea'

# Testing
print(menu)

print(type(menu))
print(len(menu))

print(type(menu['Monday']))
print(len(menu['Monday']))

print(type(menu['Monday']['breakfast']))
print(len(menu['Monday']['breakfast']))

print(type(menu['Monday']['breakfast']['main']))
print(len(menu['Monday']['breakfast']['main']))