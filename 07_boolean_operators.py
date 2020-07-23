A = 3
B = 4

print(f'{A != B}')  # A is not equal to B
print(f'{A == B}')  # A is equal to B
print(f'{A > B}')   # A is greater than B
print(f'{A >= B}')  # A is greater or equal to B
print(f'{A < B}')   # A is less than B
print(f'{A <= B}')  # A is less or equal to B
print(f'{A is B}')  # A is  B (Point to the same object)
print(f'{A is not B}')  # A is not B (Point to a different object)

# Example for is operator
first_obj = 'test1'
second_obj = 'test2'
print(f'Objects are different at the begging: {first_obj is not second_obj}')
first_obj = second_obj
print(f'After the assignment objects are equal: {first_obj is second_obj}')



