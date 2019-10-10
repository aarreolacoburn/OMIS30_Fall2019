# Class5 Homework
# author: midavis
# last modified: 2019-10-10
# OMIS 30 - Fall 2019 - HW5
# Create a menu dictionary of dictionaries...

# There are multiple ways to do this.  The instructions say to start with a blank dictionary
menu = dict()

# Method #1
# Create an empty dictionary, and then add each meal individually
menu['Monday'] = dict()
menu['Monday']['breakfast'] =   {'drink':'water', 'appetizer':'calimari', 'main':'scrambled eggs', 'dessert':'ice cream'}
menu['Monday']['lunch']     =   {'drink':'water', 'appetizer':'calimari', 'main':'Ikes', 'dessert':'ice cream'}
menu['Monday']['dinner']    =   {'drink':'water', 'appetizer':'calimari', 'main':'steak', 'dessert':'ice cream'}

# Method #2
# Create an empty dicionary, and then add all 3 meals at once
menu['Tuesday'] = dict()
menu['Tuesday'] =   {
                    'breakfast' : {'drink':'water', 'appetizer':'calimari', 'main':'omelet', 'dessert':'ice cream'},
                    'lunch'     : {'drink':'water', 'appetizer':'calimari', 'main':'Subway', 'dessert':'ice cream'},
                    'dinner'    : {'drink':'water', 'appetizer':'calimari', 'main':'burger', 'dessert':'ice cream'}
                    }

# Method #3
# Skip adding an empty dictionary, and just add all 3 meals at once
menu['Wednesday'] = {
                    'breakfast' : {'drink':'water', 'appetizer':'calimari', 'main':'pancakes', 'dessert':'ice cream'},
                    'lunch'     : {'drink':'water', 'appetizer':'calimari', 'main':'Quiznos', 'dessert':'ice cream'},
                    'dinner'    : {'drink':'water', 'appetizer':'calimari', 'main':'salmon', 'dessert':'ice cream'}
                    }

# Method 4
# Define a dictionary for just that day first and then add it to the menu dictionary
Thursday = {
                    'breakfast' : {'drink':'water', 'appetizer':'calimari', 'main':'waffles', 'dessert':'ice cream'},
                    'lunch'     : {'drink':'water', 'appetizer':'calimari', 'main':'Chipotle', 'dessert':'ice cream'},
                    'dinner'    : {'drink':'water', 'appetizer':'calimari', 'main':'falafel', 'dessert':'ice cream'}
}
menu['Thursday'] = Thursday

# Method 5
# Update method - create an empty dictionary and then use the update method
menu['Friday'] = dict()
Friday = {
                    'breakfast' : {'drink':'water', 'appetizer':'calimari', 'main':'toast', 'dessert':'ice cream'},
                    'lunch'     : {'drink':'water', 'appetizer':'calimari', 'main':'Qdoba', 'dessert':'ice cream'},
                    'dinner'    : {'drink':'water', 'appetizer':'calimari', 'main':'spaghetti', 'dessert':'ice cream'}
}
menu['Friday'].update(Friday)

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