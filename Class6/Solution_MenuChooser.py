# author: midavis
# October 15, 2019
# OMIS 30 Class 6 HW: Menu Chooser

menu = {
'Monday':
{'Breakfast': {'Drink': 'Water', 'Appetizer': 'Hash Browns', 'Main': 'Eggs', 'Dessert': 'Cupcake'},
'Lunch': {'Drink': 'Soda', 'Appetizer': 'Crisps', 'Main': 'Burger', 'Dessert': 'Pie'},
'Dinner': {'Drink': 'Milk', 'Appetizer': 'Fries', 'Main': 'Steak', 'Dessert': 'Cookies'}},

'Tuesday':
{'Breakfast': {'Drink': 'Horchata', 'Appetizer': 'Chips', 'Main': 'Burrito', 'Dessert': 'Caramel'},
'Lunch': {'Drink': 'Orange Soda', 'Appetizer': 'Takis', 'Main': 'Quesadilla', 'Dessert': 'Flan'},
'Dinner': {'Drink': 'Milk', 'Appetizer': 'Street Taco', 'Main': 'Super Burrito', 'Dessert': 'Cinnamon Twists'}},

'Wednesday':
{'Breakfast': {'Drink': 'Orange Juice', 'Appetizer': 'Tater Tots', 'Main': 'Pancakes', 'Dessert': 'Frosted Donut'},
'Lunch': {'Drink': 'Water', 'Appetizer': 'Mushroom Bundle', 'Main': 'Pad Thai', 'Dessert': 'Pineapple Fruit Cake'},
'Dinner': {'Drink': 'Beer', 'Appetizer': 'Spring Rolls', 'Main': 'Yellow Curry', 'Dessert': 'Rice Roll'}},

'Thursday':
{'Breakfast': {'Drink': 'Apple Juice', 'Appetizer': 'Mini Pizza Rolls', 'Main': 'Spaghetti', 'Dessert': 'Cannoli'},
'Lunch': {'Drink': 'Water', 'Appetizer': 'Mozzarella Sticks', 'Main': 'Penne Pasta', 'Dessert': 'Cake'},
'Dinner': {'Drink': 'Wine', 'Appetizer': 'Cheese Charcuterie', 'Main': 'Lasagna', 'Dessert': 'Croissant'} },

'Friday':
{'Breakfast': {'Drink': 'Coffee', 'Appetizer': 'Cereal', 'Main': 'Waffle', 'Dessert': 'Syrup Pancakes'},
'Lunch': {'Drink': 'Kale Juice', 'Appetizer': 'Mashed Potatoes', 'Main': 'Turkey', 'Dessert': 'Carrot Cake'},
'Dinner': {'Drink': 'Milk', 'Appetizer': 'Eggplant Bites', 'Main': 'Deep Dish Pizza', 'Dessert': 'Pizookie'}}
}

# figure out which day
    # print the list of options of days
        # find the keys in the dictionary
        # print them
print( list( menu.keys() ) )
    # ask the user which day
        # print a question to the user
print( 'Which day would like to come in?' )
    # get their answer
        # use the input function
DayOfWeek = input()

# figure out the main courses for that day and list them
    # search = use the key to get the value because you're using dictionaries
    # search the dictionary for that day
    # search the day dictionary for each of the three meals
    # search each of the meal dictionaries for the mains
    # print each of the mains out
print( menu[DayOfWeek]['Breakfast']['Main'] )
print( menu[DayOfWeek]['Lunch']['Main'] )
print( menu[DayOfWeek]['Dinner']['Main'] )

# figure out the favorite
    # ask the user for which main?
print( 'Which main would you like?' )
    # use the input function to get their answer
Main = input()

# match the favorite to the courses ***

### Solution 1 ###
# Create a dictionary of values
temp_dict = dict()
temp_dict[ menu[DayOfWeek]['Breakfast']['Main'] ] = 'Breakfast'
temp_dict[ menu[DayOfWeek]['Lunch']['Main'] ] = 'Lunch'
temp_dict[ menu[DayOfWeek]['Dinner']['Main'] ] = 'Dinner'
Meal = temp_dict[Main] 

### Solution 2 ###
# Create a list of the values and use a simple index
name_of_meals = [ 'Breakfast', 'Lunch', 'Dinner' ]
name_of_meals = list( menu[DayOfWeek].keys() )
list_of_meals = [ menu[DayOfWeek]['Breakfast']['Main'], menu[DayOfWeek]['Lunch']['Main'], menu[DayOfWeek]['Dinner']['Main'] ]
meal_index = list_of_meals.index(Main)
Meal = name_of_meals[meal_index]

### Solution 3 ###
# Go fancy and do solution 2 in one giant step
Meal = list( menu[DayOfWeek].keys() )[ [ menu[DayOfWeek]['Breakfast']['Main'], menu[DayOfWeek]['Lunch']['Main'], menu[DayOfWeek]['Dinner']['Main'] ].index(Main) ]

#### Solution 4 ###
# using if statements - which was not allowed initially
if Main == menu[DayOfWeek]['Breakfast']['Main']:
    Meal = 'Breakfast'
elif Main == menu[DayOfWeek]['Lunch']['Main']:
    Meal = 'Lunch'
elif Main == menu[DayOfWeek]['Dinner']['Main']:
    Meal = 'Dinner'



# print it out
print('You chose ' + DayOfWeek + ' ' + Meal + ' for your free meal!')