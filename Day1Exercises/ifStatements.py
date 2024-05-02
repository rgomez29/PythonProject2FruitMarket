x = 5
if x == 5:
    print ('x is equal to 5')
else:
    print('Condition failed')

if true:
    print('This conidition will always succedd')

if false:
    print('This condition will always fail')

a_string = ''
if a_string:
    print('Non-empty strings are truthy')

y = 10
if x < y:
    print('x is less than y')

z = 20
if x >= z:
    print('this will fail')
elif x == z:
    print('this will also fail')
else:
    print('If all else fails, the else branch executes.')

if x >= z or x<=y:
    print('With the or operator, if the at least one of the condituions succeeds, the entire condition succeeds')

if x >= z and x <= y:
    print("Even though x is less than or equal to y, it is not greater than or equal to z. Both conditions need to succeed with the operator")

if not x >= z:
    print('x is not greater than or equal to z.')

x = 7
if x % 3 == 0:
    print('x is a multiple of 3')
else:
    print('x is not a multiple of 3')

if x <= y < z:
    print('y is within x and z inclusive')