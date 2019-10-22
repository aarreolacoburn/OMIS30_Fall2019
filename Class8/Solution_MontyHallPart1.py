# ##################
# author: midavis
# date: 2019-10-22
#
# OMIS 30
# Fall 2019
# Class 8
# Monty Hall Part 1
# #####################################

# set up 3 doors
# ask the user to select one of them
# open another door without a prize in it
# ask the user to switch
# tell the user if they won


# use a random number generator to figure out which door is the prize
import random
winner_door = random.randint(1,3)

# set up the three doors and then name the random one true
doors = {1: False, 2: False, 3: False}
doors[winner_door] = True

# ask the user to select one of them
print('Which door would you like?')
chosen_door = int(input())

# open another door without a prize
if doors[1] == False and 1 != chosen_door:
    door_to_open = 1
elif doors[2] == False and 2 != chosen_door:
    door_to_open = 2
elif doors[3] == False and 3 != chosen_door:
    door_to_open = 3
else:
    door_to_open = 0

# list available doors
available_doors = [1,2,3]
available_doors.pop( available_doors.index(door_to_open) )
available_doors.pop( available_doors.index(chosen_door) )
switch_to_door = available_doors[0]

# ask the user to switch
print('Monty opened up door number ' + str(door_to_open) + ' and it is not the prize.')
print('Would you like to switch to door number ' + str(switch_to_door) + '? y/n')
switch = input()

# tell the user if they won
if switch == 'y':
    final_door = switch_to_door
elif switch == 'n':
    final_door = chosen_door
else: 
    final_door = 0

if doors[final_door] == True:
    print('Congratulations! You won!')
elif doors[final_door] == False:
    print('Bummer, you lost!')
else:
    print('ERROR')
