# author: midavis
# last modified: Oct 17, 2019
# OMIS 30 Fall 2019 Class 6 HW
# Convert F to C

F = 35
# sometimes python doesn't like it if you divide by integers, and only returns integers.  This way guarantees a float will be returned.
C = round( (F - 32) * 5.0 / 9, 2)
print( str(F) + " degrees in Fahrenheit is equivalent to " + str(C) + " degrees in Celsius.")