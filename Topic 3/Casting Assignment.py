"""
Program: Casting Assignment.py
Author: John Ord
Last date modified: 08/31/2022

The purpose of this program is to accept any input,
convert to a integer type and output the integer.
"""
#test case one input 7 expected answer is 27.93
test = 7
print('you bought: $' + str(float(int(test) * 3.99)))

#test case two input 4 expected answer is 15.96
test2 = 4
print('you bought: $' + str(float(int(test2) * 3.99)))

#takes user input does multiplication and converts to string for output
print('you bought: $' + str(float(int(input('Please enter number of comics purchased: ')) * 3.99)) + ' of comics')



