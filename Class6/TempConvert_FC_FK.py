# Temp Converter Multiple Ways
# F->C, F->K

F = 35

to_scale = input('what scale do you want to convert to? C or K: ')

if to_scale == 'C':
    C = (F - 32) * (5/9)
    print( str(F) + " degrees in Fahrenheit is equivalent to " + str(C) + " degrees in Celsisus." )

elif to_scale == 'K':
    K = (F - 32) * (5/9) + 273.15
    print( str(F) + " degrees in Fahrenheit is equivalent to " + str(K) + " degrees in Kelvin." )

# technically you don't need this, but it's nice
else:
    print('you did not select one of the right options')